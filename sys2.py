import tkinter as tk
import psutil
import platform

def sys_status():
    system = platform.system() + " " + platform.release()
    processor = platform.processor()
    cpu_usage = f"{psutil.cpu_percent(interval=1)}%"
    memory_usage = f"{psutil.virtual_memory().percent}%"
    disk_usage = f"{psutil.disk_usage('/').percent}%"
    return system, processor, cpu_usage, memory_usage, disk_usage

def sys_ref():
    system, processor, cpu, mem, disk = sys_status()
    
    system_label.config(text=f"System: {system}")
    processor_label.config(text=f"Processor: {processor}")
    cpu_label.config(text=f"CPU Usage: {cpu}")
    memory_label.config(text=f"Memory Usage: {mem}")
    disk_label.config(text=f"Disk Usage: {disk}")
    

    root.after(5000, sys_ref)

root = tk.Tk()
root.title("SYS Monitor")

def create_label_box(text):
    frame = tk.Frame(root, bg="white", padx=10, pady=5, bd=0)
    label = tk.Label(frame, text=text, font=("Arial", 12), bg="white", fg="black")
    label.pack(pady=5, padx=5)
    return frame, label

system_frame, system_label = create_label_box("System: ")
processor_frame, processor_label = create_label_box("Processor: ")
cpu_frame, cpu_label = create_label_box("CPU Usage: ")
memory_frame, memory_label = create_label_box("Memory Usage: ")
disk_frame, disk_label = create_label_box("Disk Usage: ")

for frame in [system_frame, processor_frame, cpu_frame, memory_frame, disk_frame]:
    frame.pack(pady=5, padx=10, fill="x")

sys_ref()
root.mainloop()
