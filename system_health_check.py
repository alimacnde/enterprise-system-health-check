# system_health_check.py

import psutil
from datetime import datetime

# Threshold for warning (percent)
THRESHOLD = 85

def check_disk():
    usage = psutil.disk_usage('/')
    percent = usage.percent
    if percent > THRESHOLD:
        print(f"[{datetime.now()}] WARNING: Disk usage at {percent}%")
    else:
        print(f"[{datetime.now()}] Disk usage OK: {percent}%")

def check_memory():
    usage = psutil.virtual_memory()
    percent = usage.percent
    if percent > THRESHOLD:
        print(f"[{datetime.now()}] WARNING: Memory usage at {percent}%")
    else:
        print(f"[{datetime.now()}] Memory usage OK: {percent}%")

if __name__ == "__main__":
    check_disk()
    check_memory()

