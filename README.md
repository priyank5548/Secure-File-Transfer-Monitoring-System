# Secure File Transfer Monitoring System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Kali%20Linux-success.svg) ![Security](https://img.shields.io/badge/Domain-Defensive%20Security%20%7C%20SOC-critical.svg) ![Status](https://img.shields.io/badge/Project-Completed-brightgreen.svg)

## 📌 Project Overview
The Secure File Transfer Monitoring System is a defensive security tool designed to ensure data confidentiality and track file movement across a system. This project provides hands-on experience in SOC monitoring and Digital Forensics by logging file activities, detecting unauthorized data movement, and verifying file integrity using cryptographic hashing. The system is cross-platform and has been successfully tested on both Windows and Kali Linux.

## ✨ Key Features
* Real-Time File System Monitoring: Uses the watchdog library to track CREATED, MODIFIED, MOVED, and DELETED events.
* File Integrity Verification: Automatically calculates SHA-256 hashes to detect tampering or unauthorized modifications.
* Exfiltration Detection: Identifies when sensitive files are moved to suspicious destinations like USB drives, cloud folders (OneDrive, Dropbox), or mounted directories based on defined policies.
* Detailed Security Auditing: Logs include timestamps, source and destination paths, hash values, user identities, and the process name responsible for the action.
* Automated Reporting: Generates a comprehensive Final Audit Report summarizing all monitored activities and detected security events.

## 🛠️ Tech Stack
* Language: Python
* Libraries:
  * watchdog – File system event monitoring
  * hashlib – SHA-256 integrity verification
  * psutil – Process and user tracking
* Environment: Tested on Windows and Kali Linux

## 📁 Project Structure
Secure_File_Monitor/
├── diagrams/           # System Architecture, Workflow, and Flowchart diagrams
├── logs/               # File event logs and security alerts
├── reports/            # Final audit reports
├── screenshots/        # Execution evidence (Windows and Linux)
├── config.json         # Monitoring rules and security policies
├── monitor.py          # Core monitoring engine
└── requirements.txt    # Project dependencies

## 🚀 Getting Started
### Installation
Install the required dependencies:
pip install -r requirements.txt

### Configuration
Edit config.json to define sensitive files and monitoring policies:
{
  "sensitive_directory": "C:/Users/YourUser/Documents/Sensitive",
  "sensitive_files": ["secret_file.txt"],
  "suspicious_destinations": ["USB", "OneDrive", "Dropbox", "mnt"],
  "hash_algorithm": "sha256"
}

### Usage
Run the monitoring system:
python monitor.py
Press CTRL + C to stop monitoring and automatically generate the Final Audit Report.

## 📊 Workflow
1. Monitor – Detects file system events in real time.
2. Classify – Identifies whether a file is marked as sensitive.
3. Verify – Computes SHA-256 hash to validate file integrity.
4. Analyze – Checks authorization and destination policies.
5. Alert / Log – Records metadata and triggers alerts for violations.
6. Report – Produces the final security audit report.

## 🛡️ Learning Outcomes
* Practical implementation of Data Loss Prevention (DLP) concepts.
* Detection techniques for Insider Threats and suspicious data transfers.
* Hands-on experience with Blue Team monitoring and real-world file auditing.
* Cross-platform defensive security tool development.

## 🏁 Conclusion
The Secure File Transfer Monitoring System demonstrates a real-world defensive security approach by combining file system monitoring, integrity verification, and policy-based alerting. The project aligns closely with SOC and digital forensics practices and serves as a strong foundation for further work in defensive cybersecurity.
