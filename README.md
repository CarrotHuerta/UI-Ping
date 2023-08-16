## IP Ping Checker with Real-Time Status Display

This Python script utilizes the `tkinter` library to create a graphical user interface (GUI) for pinging multiple IP addresses concurrently. It offers the following features:

1. Allows users to input a list of IP addresses (one per line) to monitor.
2. Performs periodic pinging of the entered IP addresses.
3. Displays real-time ping status and response times.
4. Updates the GUI with color-coded indicators for live and offline status.

### Features:

- Input a list of IP addresses to monitor their ping status.
- Real-time ping updates with colored indicators for live (✓) and offline (✗) status.
- Displays the response time (in milliseconds) for live IPs.
- Customizable GUI with separate sections for IP input and ping results.

### Usage:

1. Run the script to open the GUI window.
2. Enter the IP addresses you want to monitor, one per line, in the input area.
3. The script will continuously ping the specified IP addresses and update their status in the results area.
4. Live IPs will be marked with a green checkmark (✓), and offline IPs will be marked with a red 'x' (✗).

Note that the script uses multithreading to handle the continuous ping updates without blocking the GUI. The `tkinter` library is used to create the graphical interface, and the GUI elements are updated in real-time based on the ping results.

Feel free to modify and distribute this script according to your needs. If you encounter any issues or have suggestions for improvement, please let us know!
