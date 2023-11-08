#!/usr/bin/env python3

import time
from datetime import datetime, timedelta
from serial import Serial, SerialException
import pandas as pd

# Define the serial port and baud rate (change this to match your setup)
serial_port = 'COM10'  # Change this to your specific serial port
baud_rate = 115200  # Change this to match your printer's baud rate

# Function to send a G-code command and receive the response
def send_gcode(command, printer):
    printer.write(command.encode())
    time.sleep(0.2)  # Give the printer some time to process the command
    response = printer.readline().decode().strip()
    return response

# Function to set the hotend temperature to the desired value
def set_hotend_temperature(desired_temperature, hotend_number, printer):
    # Enforce temperature limits (30°C to 251°C)
    desired_temperature = max(30, min(251, desired_temperature))
    
    # Set the hotend temperature to the desired value for the specified hotend
    hotend_set_temp_command = f"M104 T{hotend_number} S{desired_temperature}\n"
    send_gcode(hotend_set_temp_command, printer)
    
    print(f"Hotend {hotend_number} temperature set to {desired_temperature} °C")

# Function to record hotend temperature for a duration
def record_temperature(duration_seconds, output_file, hotend_number, printer):
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=duration_seconds)

    data = []

    while datetime.now() < end_time:
        # Request the hotend temperature for the specified hotend
        hotend_temp_command = f"M105 T{hotend_number}\n"
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
            print(f"Elapsed Time (s): {elapsed_seconds}, Hotend {hotend_number} Temperature: {hotend_temperature} °C")
        else:
            print(f"Elapsed Time (s): {elapsed_seconds}, Failed to retrieve hotend {hotend_number} temperature.")

        # Wait for 1 second before the next measurement
        time.sleep(1)

    # Turn off the hotend at the end
    hotend_off_command = f"M104 T{hotend_number} S0\n"  # Turn off hotend for the specified hotend
    send_gcode(hotend_off_command, printer)

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=["Elapsed Time (s)", f"Hotend {hotend_number} Temperature (°C)"])

    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

# Create a new output Excel file with the current date and time
output_file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_temperature.xlsx")

try:
    # Open the serial connection
    # Open the serial connection
    printer = Serial(serial_port, baud_rate, timeout=2)


    # Ask the user for the desired hotend temperature, recording time, and hotend number
    input_str = input("Enter desired hotend temperature, recording time, and hotend number (e.g., '200 100 1'): ")
    desired_temperature, record_duration_seconds, hotend_number = map(float, input_str.split())
    
    # Set the hotend temperature to the desired value for the specified hotend
    set_hotend_temperature(desired_temperature, hotend_number, printer)

    with pd.ExcelWriter(output_file_name, engine="xlsxwriter") as output_file:
        record_temperature(record_duration_seconds, output_file, hotend_number, printer)

    # Close the serial connection
    printer.close()

except SerialException:
    print(f"Failed to open serial port {serial_port}. Make sure the printer is connected.")
except KeyboardInterrupt:
    print("Recording stopped by user.")
except ValueError:
    print("Invalid input format. Please enter 'temp time hotend' (e.g., '200 100 1').")
