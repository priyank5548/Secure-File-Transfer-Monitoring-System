# Secure File Transfer Monitoring System

A Blue Team / Defensive Security project that monitors file system activity, detects unauthorized file movement, verifies file integrity using cryptographic hashing, generates alerts, and produces a final audit report.

This project simulates real-world SOC, DLP (Data Loss Prevention), and Digital Forensics monitoring techniques used to detect insider threats, data exfiltration, and file tampering.

---

## Project Overview

File transfers are a major security risk in organizations. Sensitive data can be copied, moved, modified, or deleted without authorization—intentionally or accidentally.

The Secure File Transfer Monitoring System continuously monitors file system events and provides:

- File activity logging  
- Sensitive file monitoring  
- Integrity verification using SHA-256 hashing  
- Unauthorized movement detection  
- Alert generation  
- Final audit reporting  

The system works on both Linux and Windows.

---

## Key Features

- Real-time file system monitoring  
- Detects create, modify, move, and delete operations  
- Sensitive directory enforcement  
- Cryptographic integrity checks (SHA-256)  
- Policy-based authorization checks  
- Alert generation for violations  
- Automatic audit report generation  
- Cross-platform support (Linux / Windows)  

---

## Project Structure

Secure_File_Monitor  
├── monitor.py                Main monitoring engine  
├── config.json               Configuration (paths and policies)  
├── requirements.txt          Python dependencies  
├── logs  
│   ├── file_events.log       File activity logs  
│   └── alerts.log            Security alerts  
├── reports  
│   └── final_audit_report.txt    Generated audit report  
├── diagrams  
│   ├── Flowchart Diagram.png  
│   ├── System Architecture Diagram.png  
│   └── Workflow Process Flow Diagram.png  
├── screenshots  
│   ├── linux_result.png  
│   ├── windows_result.png  
│   └── final_report.png  
└── .gitignore  

---

## Architecture Overview

1. User or OS performs file operations  
2. Watchdog monitors file system events  
3. Sensitive files are identified  
4. Integrity hash (SHA-256) is calculated  
5. Authorization and policy checks are applied  
6. Logs and alerts are generated  
7. Final audit report is created  

---

## Workflow Summary

1. Monitor file system events  
2. Detect file operation (create, modify, move, delete)  
3. Identify sensitive files  
4. Perform integrity verification  
5. Check authorization and destination policy  
6. Generate logs with metadata  
7. Raise alerts on violations  
8. Generate final audit report  

---

## Tools and Technologies Used

- Programming Language: Python  
- Libraries: watchdog, hashlib, psutil (optional)  
- Operating Systems: Linux, Windows  
- Diagrams: Draw.io  

---

## Installation and Setup

1. Clone the repository  
   git clone https://github.com/your-username/Secure_File_Monitor.git  

2. Navigate to the project directory  
   cd Secure_File_Monitor  

3. Install dependencies  
   pip install -r requirements.txt  

4. Configure the sensitive directory in config.json  
   Example:  
   sensitive_directory: /home/user/Documents  
   (Use a Windows path if running on Windows)

---

## Running the Project

Run the monitoring engine:  
python monitor.py  

The system will:  
- Start monitoring the configured sensitive directory  
- Log all file activity  
- Generate alerts for violations  

Stop monitoring using CTRL + C.  
A final audit report will be generated automatically.

---

## Sample Outputs

- File Events Log: records all file operations with timestamps, user, process, and hash  
- Alerts Log: records unauthorized movements and integrity violations  
- Final Audit Report: consolidated summary of all activity and detections  

---

## Learning Outcomes

- Understanding file system monitoring  
- Implementing hash-based integrity checks  
- Detecting unauthorized data movement  
- Applying Blue Team and SOC monitoring concepts  
- Building real-world defensive security tooling  

---

## Use Cases

- Data Loss Prevention (DLP)  
- Insider Threat Detection  
- Digital Forensics Monitoring  
- Security Auditing  
- Blue Team Training Labs  

---

## Disclaimer

This project is for educational and defensive security purposes only.  
Do not deploy in production environments without proper authorization and hardening.

---

## Author

Developed as a practical cybersecurity project focused on defensive monitoring, auditing, and incident detection.
