# Secure File Transfer Monitoring System

A lightweight, cross-platform file monitoring toolkit focused on visibility, integrity verification, and policy-based detection of sensitive file movement.  
The project is intended for practical use, learning, and evaluation in defensive security, SOC monitoring, and digital forensics contexts.

---

## Overview

File transfers and file modifications are common sources of data leakage, insider misuse, and integrity violations. This toolkit monitors file system activity in real time, records detailed audit logs, and applies configurable rules to identify suspicious or unauthorized behavior.

The system emphasizes clarity and reliability over complexity. It does not attempt to block activity or perform offensive actions; its purpose is monitoring, logging, and reporting.

The toolkit has been tested on Windows and Kali Linux.

---

## What the Tool Does

- Monitors file system events such as creation, modification, movement, and deletion  
- Tracks sensitive files and directories defined by policy  
- Verifies file integrity using SHA-256 hashing  
- Detects movement of sensitive files to suspicious destinations (for example removable media or cloud-synced folders)  
- Records detailed audit logs with timestamps, paths, user context, and process information  
- Produces a consolidated audit report when monitoring is stopped  

---

## Intended Use

This project is suitable for:
- Defensive security demonstrations and labs  
- SOC monitoring practice  
- Digital forensics and audit exercises  
- Academic or training environments  

It is not designed as malware, an intrusion tool, or a prevention system.

---

## Technology Stack

- Language: Python  
- Libraries:
  - watchdog for file system event monitoring  
  - hashlib for cryptographic hashing (SHA-256)  
  - psutil for process and user context  
- Platforms: Windows and Kali Linux  

---

## Project Layout

Secure_File_Monitor/
- diagrams/        System architecture, workflow, and flowchart diagrams  
- logs/            File event logs and alert records  
- reports/         Generated audit reports  
- screenshots/     Execution evidence on supported platforms  
- config.json      Monitoring rules and policy configuration  
- monitor.py       Main monitoring script  
- requirements.txt Python dependencies  

---

## Installation

1. Ensure Python 3 is installed.
2. Install dependencies listed in requirements.txt.

Example:
pip install -r requirements.txt

---

## Configuration

Monitoring behavior is controlled through config.json. Typical configuration includes:
- The directory to monitor
- A list of sensitive files
- Destination keywords considered suspicious
- The hashing algorithm used for integrity checks

Adjust paths according to the operating system and environment where the tool is deployed.

---

## Usage

Start monitoring by running:
python monitor.py

Monitoring continues until interrupted. When stopped, the tool automatically generates a final audit report summarizing all recorded activity.

---

## How It Works (High Level)

1. File system events are captured in real time  
2. Events are evaluated against the configured sensitive file list  
3. File integrity is verified using cryptographic hashes  
4. Destination and policy checks are applied  
5. Events and alerts are logged  
6. A final audit report is generated for review  

Detailed diagrams illustrating this flow are available in the diagrams directory.

---

## Output

- Event logs recording all monitored file activity  
- Alert logs for policy violations or integrity issues  
- A final audit report suitable for review or documentation  

An empty alert log indicates that no violations were detected during the monitoring period.

---

## Notes

- On Linux systems, temporary files created by editors during safe-write operations may appear in logs. This is expected behavior.  
- Hash verification is not performed on deleted files, as content is no longer accessible at that stage.  

---

## Conclusion

This toolkit provides a practical approach to observing and auditing file system behavior with minimal assumptions and clear output. It is intended to be understandable, configurable, and easy to extend for further defensive security experimentation or learning.
