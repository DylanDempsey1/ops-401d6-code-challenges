#!/usr/bin/python3

# Challenge 11
# Dylan Dempsey
# 05/01/23
# Create a TCP Port Range Scanner that tests whether a TCP port is open or closed

# Main


from scapy.all import *
import sys

# Define the target host and port range
target_host = "192.168.1.1"  # Replace with the target IP address
start_port = 1
end_port = 100

# Function to send a SYN packet and check for the response
def tcp_scan(target_host, target_port):
    # Create a SYN packet
    ip = IP(dst=target_host)
    syn = TCP(dport=target_port, flags='S')
    packet = ip/syn

    # Send the SYN packet and wait for a response
    response = sr1(packet, timeout=2, verbose=0)

    if response:
        # Check if the flag is 0x12 (SYN+ACK)
        if response[TCP].flags == 0x12:
            # Send a RST packet to gracefully close the connection
            rst = TCP(dport=target_port, flags='R')
            send(ip/rst, verbose=0)
            return "open"
        # Check if the flag is 0x14 (RST)
        elif response[TCP].flags == 0x14:
            return "closed"
    else:
        return "filtered"

# Scan the specified port range
for port in range(start_port, end_port + 1):
    port_status = tcp_scan(target_host, port)
    print(f"Port {port} is {port_status}")
    
    # End
    
    # ChatGPT was referenced for this code
