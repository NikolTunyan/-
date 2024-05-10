import os
import shutil
import tkinter as tk
from tkinter import filedialog

    # Define the list of signatures (functions in potential viruses)
virus_signatures = [
        "hack()",
        "hacknow()",
        "deletesystem()",
        "blockall()",
        "Virus Load Simulation",
        "encrypt_files()",
        "steal_credentials()",
        "send_data_to_server()",
        "keylogger_start()",
        "webcam_access()",
        "microphone_access()",
        "spread_to_network()",
        "modify_system_files()",
        "launch_ddos_attack()",
        "ransomware_encrypt()",
        "record_keystrokes()",
        "bypass_firewall()",
        "create_backdoor()",
        "delete_user_accounts()",
        "disable_antivirus()",
        "inject_malicious_code()",
        "launch_cryptocurrency_miner()",
        "spoof_emails()",
        "intercept_network_traffic()",
        "elevate_privileges()",
        "tamper_with_registry()",
        "launch_botnet_attack()",
        "delete_system_files()",
        "intercept_bank_transactions()",
        "collect_personal_information()",
        "launch_brute_force_attack()",
        "modify_browser_settings()",
        "create_botnet()",
        "upload_sensitive_files()",
        "hijack_browser_sessions()",
        "launch_remote_code_execution()",
        "install_additional_malware()",
        "perform_man-in-the-middle_attack()",
        "disable_firewall()",
        "disable_system_updates()",
        "disable_security_policies()",
        "delete_critical_system_files()",
        "create_fake_login_screens()",
        "bypass_authentication()",
        "intercept_encrypted_communications()",
        "exploit_remote_code_execution_vulnerabilities()",
        "disable_backup_services()",
        "launch_worm_spread()",
        "encrypt_system_bootloader()",
        "modify_host_file()",
        "alter_system_startup_settings()",
        "hide_files_and_directories()",
        "delete_system_restore_points()",
        "corrupt_system_registry()",
        "exploit_zero-day_vulnerabilities()"
    ]

    # Define the list of filenames or patterns to exclude from quarantine
quarantine_exceptions = ["ssss.py"]

    # Define the list of folder names to exclude from quarantine
quarantine_folder_exceptions = ["D:/a/quarantine"]

    # Manually specify the quarantine folder path
quarantine_folder = "D:/a/quarantine"  # Replace with your desired path

    # Set to store paths of quarantined files
quarantined_files = set()

        # Function to check if a file is infected
def is_infected(filepath):
        with open(filepath, 'r', encoding='latin-1') as file:
            contents = file.read()
            for signature in virus_signatures:
                if signature in contents:
                    return signature  # Return the specific signature detected
        return None  # Return None if no virus signature is found

    # Function to scan files in a directory (including subdirectories)
def scan_directory(directory):
        scanned_files = 0
        viruses_found = 0
        for root, dirs, files in os.walk(directory):  # Recursively walk through all directories and files
            # Exclude quarantine folder from search
            if os.path.basename(root) in quarantine_folder_exceptions:
                continue
            for filename in files:
                filepath = os.path.join(root, filename)
                scanned_files += 1
                if is_infected(filepath) and filename not in quarantine_exceptions and filepath not in quarantined_files:
                    viruses_found += 1
                    # Move infected file to quarantine folder and create metadata
                    quarantine_file(filepath)
                    quarantined_files.add(filepath)  # Add file path to set of quarantined files
                    print(f"File {filename} moved to quarantine and disabled from system processes.")
            
        return scanned_files, viruses_found

# Function to quarantine a file and create metadata text file
def quarantine_file(filepath):
    filename = os.path.basename(filepath)
    # Move infected file to quarantine folder
    shutil.move(filepath, os.path.join(quarantine_folder, filename))
    # No need to create metadata text file

# Function to start the search
def start_search():
    directory = directory_entry.get()
    if not os.path.exists(quarantine_folder):
        os.makedirs(quarantine_folder)
    scanned_files, viruses_found = scan_directory(directory)
    result_label.config(text=f"Scanned files: {scanned_files}\nViruses found: {viruses_found}\nScanning completed.")

# Create the main window
root = tk.Tk()
root.title("Pseudo-Antivirus Program")

# Create and place the interface elements
canvas = tk.Canvas(root, height=600, width=800, bg='#102542')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

directory_label = tk.Label(frame, text="Enter directory path:", bg='white')
directory_label.pack()

directory_entry = tk.Entry(frame, width=50)
directory_entry.pack(pady=10)

start_button = tk.Button(frame, height=2, width=9, text="Start Search", command=start_search, bg='#4CAF50', fg='white', relief='flat')
start_button.pack(pady=5)

result_label = tk.Label(frame, text="", bg='white')
result_label.pack(pady=5)

progress_label = tk.Label(frame, text="", bg='white')
progress_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()