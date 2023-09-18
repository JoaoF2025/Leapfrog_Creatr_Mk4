#!/usr/bin/env python3

import serial
import time
from datetime import datetime, timedelta
import pandas as pd

# Define the serial port and baud rate (change this to match your setup)
serial_port = '/dev/ttyACM0'  # Change this to your specific serial port (Windows: 'COMx')
baud_rate = 115200  # Change this to match your printer's baud rate

# Function to send a G-code command and receive the response
def send_gcode(command, printer):
    printer.write(command.encode())
    time.sleep(0.2)  # Give the printer some time to process the command
    response = printer.readline().decode().strip()
    return response

# Function to set the hotend temperature to the desired value
def set_hotend_temperature(desired_temperature, printer):
    # Enforce temperature limits (30°C to 251°C)
    desired_temperature = max(30, min(251, desired_temperature))
    
    # Set the hotend temperature to the desired value
    hotend_set_temp_command = f"M104 S{desired_temperature}\n"
    send_gcode(hotend_set_temp_command, printer)
    
    print(f"Hotend temperature set to {desired_temperature} °C")

# Function to record hotend temperature for a duration
def record_temperature(duration_seconds, output_file, printer):
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=duration_seconds)

    data = []

    while datetime.now() < end_time:
        # Request the hotend temperature
        hotend_temp_command = "M105\n"  # Send M105 to request temperature
        response = send_gcode(hotend_temp_command, printer)

        # Extract the hotend temperature value from the response
        hotend_temperature = None
        parts = response.split(" ")
        for part in parts:
            if part.startswith("T:"):
                hotend_temperature = float(part.split("T:")[1])

        # Calculate the elapsed time in seconds
        elapsed_seconds = (datetime.now() - start_time).total_seconds()

        # Save the hotend temperature value and elapsed time to the data list
        if hotend_temperature is not None:
            data.append([elapsed_seconds, hotend_temperature])
            print(f"Elapsed Time (s): {elapsed_seconds}, Hotend Temperature: {hotend_temperature} °C")
        else:
            print(f"Elapsed Time (s): {elapsed_seconds}, Failed to retrieve hotend temperature.")

        # Wait for 1 second before the next measurement
        time.sleep(0.8)

    # Turn off the hotend at the end
    hotend_off_command = "M104 S0\n"  # Turn off hotend
    send_gcode(hotend_off_command, printer)

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=["Elapsed Time (s)", "Hotend Temperature (°C)"])

    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

# Create a new output Excel file with the current date and time
output_file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_temperature.xlsx")

try:
    # Open the serial connection
    printer = serial.Serial(serial_port, baud_rate, timeout=2)

    # Ask the user for the desired hotend temperature
    desired_temperature = float(input("Enter the desired hotend temperature (30°C to 251°C): "))
    
    # Set the hotend temperature to the desired value
    set_hotend_temperature(desired_temperature, printer)

    with pd.ExcelWriter(output_file_name, engine="xlsxwriter") as output_file:
        record_duration_seconds = 300  # Change this to the desired duration in seconds
        record_temperature(record_duration_seconds, output_file, printer)

    # Close the serial connection
    printer.close()

except serial.SerialException:
    print(f"Failed to open serial port {serial_port}. Make sure the printer is connected.")
except KeyboardInterrupt:
    print("Recording stopped by user.")
except ValueError:
    print("Invalid input for desired temperature. Please enter a valid number between 30°C and 251°C.")
