
## Temperature Logger for 3D Printers

This small python script was created with the purpose of recording the temperatures of a 3D printer's hotend.


## Installation

To use this script, whether it's the Linux or Windows version, you need to install two libraries. This installation can be done using the following commands:

```bash
  pip install pyserial
  pip install pandas
```

In addition to installing these libraries, you also need to change the serial port, described in line 9 of the script, to the port being used by the printer.

```bash
serial_port = '/dev/ttyACM0'  # Change this to your specific serial port in the Linux Version
```
```bash
serial_port = 'COM10'  # Change this to your specific serial port in the Windows Version
```
## Usage

To run the script after installing all dependencies, simply use the following command in the Linux terminal.

```bash
./Temperature_Logger.py
```

Similarly, to use the script on Windows, you can run the following command in the console.

```bash
python3 Temperature_Logger_Windows.py
```

Alternatively, the script can be run from the console within Visual Studio Code or PyCharm.

Upon opening the script, it will prompt you to set the desired heating temperature (in °C), the sampling time (in seconds), meaning how long the data acquisition should be done, and finally, which hotend to use (T0 for the case where the printer has only 1 hotend), as shown in the following example:

```bash
Enter desired hotend temperature, recording time, and hotend number (e.g., '200 100 1'): 250 60 0
```

After correctly entering the requested data, the console will display all temperatures as they are recorded.

At the end of the measurement, an ```.xlsx``` file will be created with the values obtained by the script. This file will be saved in the same folder as the script, and its name will be the date and time of its creation, as shown in the example:

```bash
(year-month-day_hour_minutes_seconds_temperature.xlsx)
```

## Authors

- [@JoaoF2025](https://github.com/JoaoF2025)

