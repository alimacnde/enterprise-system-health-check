import shutil
import psutil
from datetime import datetime

LOG_FILE = "health_log.txt"

def write_log(message):
    """Append a timestamped message to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

def check_disk_usage():
    """Check current disk usage percentage."""
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100

    write_log(f"Disk usage: {percent_used:.2f}%")

    if percent_used > 85:
        write_log("WARNING: Disk usage is above 85%")

def check_memory_usage():
    """Check current memory usage percentage."""
    memory = psutil.virtual_memory()

    write_log(f"Memory usage: {memory.percent}%")

    if memory.percent > 85:
        write_log("WARNING: Memory usage is above 85%")

def run_health_check():
    write_log("Starting system health check")

    check_disk_usage()
    check_memory_usage()

    write_log("Health check completed\n")

if __name__ == "__main__":
    run_health_check()
