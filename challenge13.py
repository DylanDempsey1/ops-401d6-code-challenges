#!/use/bin/python3

# Challenge 13
# Dylan Dempsey
# 05/03/23
# Combine the two modes (port and ping) of your network scanner script.

# Main

# Iport required modules
import socket
import os
import sys
import platform
from datetime import datetime
from ping3 import ping

# Function to check if a host is responsive using ICMP echo requests
def is_host_responsive(ip):
    try:
        # Send an ICMP echo request to the target IP and receive the response time
        response = ping(ip, timeout=2)
        # If the response time is not None, the host is considered responsive
        if response is not None:
            return True
    except Exception as e:
        # If there is an error, print the error message
        print(f"Error: {e}")
    # If the host is not responsive, return False
    return False

# Function to perform a port scan on a given IP address
def port_scan(ip):
    # Print the target IP address
    print(f"Scanning ports for {ip}")
    # Record the start time of the port scanning
    start_time = datetime.now()
    try:
        # Iterate through ports 1 to 1024
        for port in range(1, 1025):
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the socket connection attempt
            sock.settimeout(1)
            # Attempt to connect to the target IP and port
            result = sock.connect_ex((ip, port))
            # If the result is 0, the port is open
            if result == 0:
                print(f"Port {port}: Open")
            # Close the socket
            sock.close()
    except KeyboardInterrupt:
        # If the user presses Ctrl+C, exit the script
        print("Exiting...")
        sys.exit()
    except socket.gaierror:
        # If the hostname cannot be resolved, print an error message and exit the script
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        # If there's a connection error, print an error message and exit the script
        print("Could not connect to server.")
        sys.exit()
    # Record the end time of the port scanning
    end_time = datetime.now()
    # Calculate the total time taken for port scanning
    total_time = end_time - start_time
    # Print the total time taken
    print(f"Scanning completed in {total_time}")

# Main function
if __name__ == "__main__":
    # Prompt the user for the target IP address
    target_ip = input("Enter the IP address to scan: ")

    # Check if the target IP is responsive using the is_host_responsive function
    if is_host_responsive(target_ip):
        # If the IP is responsive, print the status and start the port scan
        print(f"{target_ip} is responsive. Starting port scan...")
        port_scan(target_ip)
    else:
        # If the IP is not responsive, print the status and exit the script
        print(f"{target_ip} is not responsive. Exiting...")
        
        # End
        
        # ChatGPT was referenced for this code.
