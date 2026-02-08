# Secure File Transfer Monitoring System

A Blue Team / Defensive Security project that monitors file system activity, detects unauthorized file movement, verifies file integrity using cryptographic hashing, generates alerts, and produces a final audit report.

This project demonstrates real-world SOC, DLP (Data Loss Prevention), and Digital Forensics monitoring techniques used to detect insider threats, data exfiltration, and file tampering.

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

The system is designed to be cross-platform and works on both Linux and Windows.

---

## Key Features

- Real-time file system monitoring  
- Detection of create, modify, move, and delete operations  
- Sensitive directory enforcement  
- Cryptographic integrity checks (SHA-256)  
- Policy-based authorization validation  
- Security alert generation  
- Automatic audit report creation  
- Cross-platform compatibility  

---

## Project Structure

Secure_File_Monitor  
├── monitor.py – main monitoring engine  
├── config.json – configuration for sensitive paths and policies  
├── requirements.txt – Python dependencies  
├── logs  
│   ├── file_events.log – file activity logs  
│   └── alerts.log – security alerts  
├── reports  
│   └── final_audit_report.txt – generated audit report  
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

1. File system activity is monitored in real time  
2. Events are classified based on sensitivity  
3. Cryptographic hash values are calculated  
4. Authorization and policy rules are applied  
5. All actions are logged with metadata  
6. Alerts are generated for violations  
7. A final audit report is produced  

---

## Workflow Summary

1. Monitor file system events  
2. Identify file operation type  
3. Check if the file is sensitive  
4. Perform integrity verification  
5. Validate authorization and destination rules  
6. Log the event details  
7. Generate alerts for policy violations  
8. Produce a final audit report  

---

## Tools and Technologies Used

- Programming Language: Python  
- Libraries: watchdog, hashlib, psutil (optional)  
- Operating Systems: Linux, Windows  
- Diagram Design: Draw.io  

---

## Installation and Setup

1. Clone the repository  
   git clone https://github.com/priyank5548/Secure_File_Monitor.git  

2. Navigate to the project directory  
   cd Secure_File_Monitor  

3. Install dependencies  
   pip install -r requirements.txt  

4. Configure the sensitive directory in config.json  
   Use a placeholder path value such as:  
   <SENSITIVE_DIRECTORY>  

---

## Running the Project

Start the monitoring engine:  
python monitor.py  

The system will:
- Monitor the configured sensitive directory  
- Log all file activity  
- Generate alerts for unauthorized behavior  

Stop the program using CTRL + C.  
A final audit report is generated automatically on exit.

---

## Sample Outputs

- File Events Log: detailed records of all file operations  
- Alerts Log: unauthorized movements and integrity violations  
- Final Audit Report: consolidated summary of monitored activity  

---

## Learning Outcomes

- File system monitoring fundamentals  
- Hash-based integrity verification  
- Unauthorized data movement detection  
- Blue Team and SOC monitoring practices  
- Defensive security tool development  

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
Do not deploy in production environments without proper authorization.

---

## Author

Developed as a practical cybersecurity project focused on defensive monitoring, auditing, and incident detection.
