import tkinter as tk
import psutil
import time
import math

is_running = True

def hack():
    print("")

def complex_calculations():
    def inner_function(x):
        # Use a different calculation for larger numbers
        if x > 100:  # Adjust threshold as needed
            return x**2 + x * math.log2(x)
        else:
            return math.factorial(x) + math.sqrt(x) * math.log10(x)

    a = 2.71828
    for i in range(1, 5000000):
        a = inner_function(i) + a ** (1/i) + i * math.sin(i) * math.cos(i)

def update_load():
    if is_running:
        complex_calculations()
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        load_label.config(text=f"CPU: {cpu_usage:.2f}%  Memory: {memory_usage:.2f}%")
    root.after(2000, update_load)  # Update every 2000 milliseconds

def start_stop():
    global is_running
    is_running = not is_running
    if is_running:
        start_button.config(text="Pause")
    else:
        start_button.config(text="Start")

def end_program():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Virus Load Simulation")

# Create label for load display
load_label = tk.Label(root, text="CPU: 0.00%  Memory: 0.00%")
load_label.pack(pady=20)  # Add padding for visual spacing 

# Create buttons with styling
button_font = ('Arial', 14, 'bold')  # Larger font
button_width = 15                # Wider buttons

start_button = tk.Button(root, text="Pause", font=button_font, width=button_width, command=start_stop)
start_button.pack(pady=10) 
end_button = tk.Button(root, text="End Program", font=button_font, width=button_width, command=end_program)
end_button.pack(pady=10)

# Center buttons
start_button.pack(expand=True)
end_button.pack(expand=True)

# Start update loop
update_load()

root.mainloop()