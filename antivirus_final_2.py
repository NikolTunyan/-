import psutil
import time
from datetime import datetime, timedelta

# Manually specified safe processes (green)
SAFE_PROCESSES = ["explorer.exe", "chrome.exe", "svchost.exe"]  # Add more as needed

def analyze_process(process):
    try:
        # Process name and path
        process_name = process.name()
        process_path = process.exe()  # May require additional permissions

        # CPU usage check
        cpu_usage = process.cpu_percent(interval=1)
        if cpu_usage > 20:
            priority = "Yellow"

            # Check creation time
            creation_time = datetime.fromtimestamp(process.create_time())
            if datetime.now() - creation_time < timedelta(days=7):
                priority = "Orange"

                # Check file size (approximate, may require adjustments)
                try:
                    file_size = process.memory_info().rss / (1024 * 1024)
                    if file_size < 10:
                        priority = "Red"
                except psutil.AccessDenied:
                    pass  # Handle permission errors
            
        else:
            priority = "Green"

        # Log information based on priority
        with open("meta.logs.txt", "a") as f:
            if priority == "Green":
                f.write(f"[GREEN] {process_name}\n")
            elif priority == "Yellow":
                f.write(f"[YELLOW] {process_name} ({process_path})\n")
            elif priority == "Orange":
                f.write(f"[ORANGE] {process_name} ({process_path}), CPU: {cpu_usage:.2f}%, Created: {creation_time}\n")
            else:  # Red
                f.write(f"[RED] {process_name} ({process_path}), CPU: {cpu_usage:.2f}%, Created: {creation_time}, Size: {file_size:.2f}MB\n")

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass  # Handle exceptions for terminated processes or access issues

def scan_processes():
    for proc in psutil.process_iter(['pid', 'name', 'username', 'create_time']):
        if proc.name() not in SAFE_PROCESSES:
            analyze_process(proc)

while True:
    scan_processes()
    #time.sleep(1)  # Check every second