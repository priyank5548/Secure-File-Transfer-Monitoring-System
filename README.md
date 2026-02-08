# Secure File Transfer Monitoring System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Kali%20Linux-success.svg)
![Domain](https://img.shields.io/badge/Domain-Defensive%20Security%20%7C%20SOC-critical.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

## Project Overview
The Secure File Transfer Monitoring System is a defensive security tool designed to monitor file system activity, track sensitive file movement, and detect potential data exfiltration or tampering. The project provides practical exposure to SOC monitoring, Blue Team practices, and Digital Forensics by maintaining detailed audit logs and integrity verification using cryptographic hashing.  
The system is cross-platform and has been tested on both Windows and Kali Linux.

## Why This Project
Unauthorized file movement and data leakage are common security risks in enterprise environments. This project demonstrates how continuous file monitoring and policy-based controls can help detect insider threats, suspicious transfers, and integrity violations in real time.

## Key Features
- Real-time file system monitoring for CREATE, MODIFY, MOVE, and DELETE events
- File integrity verification using SHA-256 hashing
- Detection of sensitive file movement to suspicious destinations (USB, cloud folders, mounted paths)
- Detailed security auditing with timestamps, paths, hash values, user identity, and process name
- Automated generation of a final audit report summarizing all activities and alerts

## Tech Stack
- Language: Python  
- Libraries:
  - watchdog – File system event monitoring
  - hashlib – SHA-256 integrity verification
  - psutil – Process and user tracking
- Environment: Tested on Windows and Kali Linux

## Project Structure
```
Secure_File_Monitor/
├── diagrams/            # System architecture, workflow, and flowchart diagrams
├── logs/                # File event logs and security alerts
├── reports/             # Final audit reports
├── screenshots/         # Execution evidence (Windows & Linux)
├── config.json          # Monitoring rules and security policies
├── monitor.py           # Core monitoring engine
└── requirements.txt     # Project dependencies
```

## Getting Started

### Installation
Install the required dependencies:
```
pip install -r requirements.txt
```

### Configuration
Edit `config.json` to define sensitive files and monitoring policies:
```
{
  "sensitive_directory": "C:/Users/YourUser/Documents/Sensitive",
  "sensitive_files": ["secret_file.txt"],
  "suspicious_destinations": ["USB", "OneDrive", "Dropbox", "mnt"],
  "hash_algorithm": "sha256"
}
```

### Usage
Run the monitoring system:
```
python monitor.py
```
Press **CTRL + C** to stop monitoring and automatically generate the final audit report.

## Workflow
1. Monitor – Detects file system events in real time  
2. Classify – Identifies whether a file is marked as sensitive  
3. Verify – Computes SHA-256 hash to validate file integrity  
4. Analyze – Checks authorization and destination policies  
5. Alert / Log – Records metadata and triggers alerts for violations  
6. Report – Produces the final security audit report  

## Learning Outcomes
- Practical implementation of Data Loss Prevention (DLP) concepts
- Detection techniques for insider threats and suspicious data transfers
- Hands-on experience with Blue Team monitoring and real-world file auditing
- Cross-platform defensive security tool development

## Conclusion
The Secure File Transfer Monitoring System demonstrates a real-world defensive security approach by combining file system monitoring, integrity verification, and policy-based alerting. It aligns closely with SOC and digital forensics practices and provides a strong foundation for further work in defensive cybersecurity.
