import os
import time
import json
import hashlib
import logging
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import psutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

with open("config.json", "r") as f:
    CONFIG = json.load(f)

SENSITIVE_DIR = os.path.normpath(CONFIG["sensitive_directory"])
SENSITIVE_FILES = CONFIG["sensitive_files"]
SUSPICIOUS_DESTS = CONFIG["suspicious_destinations"]

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "file_events.log"),
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

alert_logger = logging.getLogger("alerts")
alert_handler = logging.FileHandler(os.path.join(LOG_DIR, "alerts.log"))
alert_logger.addHandler(alert_handler)

def compute_hash(path):
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except:
        return "HASH_FAILED"

def is_sensitive(path):
    filename = os.path.basename(path)
    return filename in SENSITIVE_FILES

def is_suspicious_path(path):
    return any(x.lower() in path.lower() for x in SUSPICIOUS_DESTS)

def get_user_process():
    try:
        p = psutil.Process(os.getpid())
        return p.username(), p.name()
    except:
        return "unknown", "unknown"

class MonitorHandler(FileSystemEventHandler):

    def handle_event(self, event, action):
        if event.is_directory:
            return

        path = event.src_path
        filename = os.path.basename(path)
        timestamp = datetime.now().isoformat()
        user, process = get_user_process()
        file_hash = compute_hash(path)

        log = f"{action} | {path} | HASH={file_hash} | USER={user} | PROCESS={process}"
        logging.info(log)

        if is_sensitive(path) and is_suspicious_path(path):
            alert = f"ALERT: Sensitive file exfiltration detected → {path}"
            alert_logger.warning(alert)
            print(f"[ALERT] {alert}")

    def on_created(self, event):
        self.handle_event(event, "CREATED")

    def on_modified(self, event):
        self.handle_event(event, "MODIFIED")

    def on_deleted(self, event):
        self.handle_event(event, "DELETED")

    def on_moved(self, event):
        logging.info(
            f"MOVED | FROM {event.src_path} TO {event.dest_path}"
        )
        if is_sensitive(event.src_path) and is_suspicious_path(event.dest_path):
            alert_logger.warning(
                f"ALERT: Sensitive file moved to unauthorized location → {event.dest_path}"
            )

def generate_report():
    report_path = os.path.join(REPORT_DIR, "final_audit_report.txt")
    with open(report_path, "w") as r:
        r.write("SECURE FILE TRANSFER MONITORING – FINAL AUDIT REPORT\n")
        r.write("=" * 60 + "\n\n")

        r.write("FILE EVENTS:\n")
        with open(os.path.join(LOG_DIR, "file_events.log")) as f:
            r.write(f.read())

        r.write("\n\nALERTS:\n")
        if os.path.exists(os.path.join(LOG_DIR, "alerts.log")):
            with open(os.path.join(LOG_DIR, "alerts.log")) as f:
                r.write(f.read())
        else:
            r.write("No alerts detected.\n")

if __name__ == "__main__":
    observer = Observer()
    handler = MonitorHandler()
    observer.schedule(handler, SENSITIVE_DIR, recursive=True)
    observer.start()

    print("[+] Monitoring sensitive directory:")
    print(f"    {SENSITIVE_DIR}")
    print("[+] Press CTRL+C to stop and generate report")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        generate_report()
        print("[+] Monitoring stopped")
        print("[+] Final audit report generated")

    observer.join()
