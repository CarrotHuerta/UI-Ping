import tkinter as tk
import threading
import subprocess
import re
import time

def ping_ip(ip):
    try:
        process = subprocess.Popen(["ping", "-n", "3", "-w", "1000", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        output = output.decode("utf-8")
        if "Reply from" in output:
            match = re.search(r"time=(\d+)ms", output)
            if match:
                ping_time = match.group(1)
            else:
                ping_time = "<1"
            return True, ping_time
        else:
            return False, "N/A"
    except Exception:
        return False, "N/A"

def update_status():
    while True:
        result_text.delete(1.0, tk.END)  # Clear previous results

        ips = ip_entry.get("1.0", tk.END).strip().split("\n")
        processes = []
        for ip in ips:
            ip = ip.strip()
            if ip:
                process = subprocess.Popen(["ping", "-n", "3", "-w", "1000", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                processes.append((ip, process))

        for ip, process in processes:
            output, error = process.communicate()
            output = output.decode("utf-8")
            if "Reply from" in output:
                match = re.search(r"time=(\d+)ms", output)
                if match:
                    ping_time = match.group(1)
                else:
                    ping_time = "<1"
                alive = True
            else:
                ping_time = "N/A"
                alive = False

            if alive:
                status = "✓"
                status_color = "green"
            else:
                status = "✗"
                status_color = "red"

            result_text.insert(tk.END, f"{status} {ip}: Ping = {ping_time} ms\n", status_color)

        time.sleep(1)

# Create the main window
root = tk.Tk()
root.title("IP Ping Checker")

# Create and place GUI elements
ip_label = tk.Label(root, text="Enter IPs (one per line):")
ip_label.pack()

ip_entry = tk.Text(root, height=5, width=30)
ip_entry.pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

# Configure text tags for coloring and formatting
result_text.tag_configure("green", foreground="green", font=("Helvetica", 10))
result_text.tag_configure("red", foreground="red", font=("Helvetica", 10))

# Start the update thread
update_thread = threading.Thread(target=update_status)
update_thread.daemon = True
update_thread.start()

root.mainloop()