#!/usr/bin/python3

# Challenge 12
# Dylan Dempsey
# 05/02/23
# Add the following features to your Network Security Tool:

# User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
# ICMP Ping Sweep tool
# Prompt user for network address including CIDR block, for example “10.10.0.0/24”

# Create a list of all addresses in the given network
# Ping all addresses on the given network except for network address and broadcast address
# If no response, inform the user that the host is down or unresponsive.
# If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
# Otherwise, inform the user that the host is responding.
# Count how many hosts are online and inform the user.

# Main

# Print the menu and get the user's choice
def print_menu():
    # Display the available modes for the Network Security Tool
    print("Please choose a mode for the Network Security Tool:")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    
    # Get the user's choice and return it as an integer
    choice = int(input("Enter your choice (1 or 2): "))
    return choice

# Store the user's choice in the 'mode' variable
mode = print_menu()

# Import required libraries
import os
import socket
import struct
import sys
from ipaddress import IPv4Network
import subprocess

# Define the ICMP Ping Sweep function
def icmp_ping_sweep(network_address):
    # Create an IPv4Network object from the user-provided network address
    network = IPv4Network(network_address, strict=False)
    
    # Generate a list of all possible host addresses in the network
    hosts = list(network.hosts())
    # Initialize a counter for online hosts
    online_hosts = 0

    # Iterate through each host address
    for host in hosts:
        # Send a single ICMP echo request and store the response in 'response'
        response = os.system(f"ping -c 1 -W 1 {host} > /dev/null 2>&1")

        # Check the response and print the appropriate message
        if response == 0:
            print(f"{host} is responding.")
            online_hosts += 1
        elif response == 256:
            print(f"{host} is blocking ICMP traffic.")
        else:
            print(f"{host} is down or unresponsive.")

    # Print the total number of online hosts
    print(f"{online_hosts} hosts are online.")

# Check the user's choice and execute the corresponding function
if mode == 2:
    # Get the user's network address input with CIDR block
    network_address = input("Enter the network address with CIDR block (e.g., 10.10.0.0/24): ")
    
    # Call the ICMP Ping Sweep function with the provided network address
    icmp_ping_sweep(network_address)

elif mode == 1:
    # Add your existing code for TCP Port Range Scanner here
    pass
else:
    # Print an error message and exit if the user's choice is invalid
    print("Invalid choice. Exiting.")
    sys.exit()

# End

# ChatGPT was referenced for this code.
