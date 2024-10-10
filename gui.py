import serial
import tkinter as tk

# Function to update sensor value label
def update_sensor_value():
    if ser.in_waiting:
        sensor_value = ser.readline().decode().strip()  # Read serial data
        sensor_label.config(text=f"Sensor Value: {sensor_value}")  # Update label
    root.after(100, update_sensor_value)  # Schedule the next update

# Serial port configuration
ser = serial.Serial('COM3', 9600)  # Update 'COM3' with your port
root = tk.Tk()
root.title("Sensor GUI")

# Create GUI
sensor_label = tk.Label(root, text="Sensor Value: ")
sensor_label.pack(pady=10)

# Start updating sensor value
update_sensor_value()

root.mainloop()
