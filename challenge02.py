#!/usr/bin/python3

# Challenge 02
# Dylan Dempsey
# 04/27/23
# Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

# Main

import time
from datetime import datetime
from ping3 import ping, exceptions

def icmp_ping(host):
    try:
        # Transmit a single ICMP packet
        response_time = ping(host, timeout=2)
        
        if response_time is not None:
            return "Network Active"
        else:
            return "Network Down"
    
    except exceptions.PingError as e:
        return f"Error: {e}"

def main():
    host = "8.8.8.8"  # Replace this with the target IP address
    while True:
        status = icmp_ping(host)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"{timestamp} {status} to {host}")
        
        # Wait for 2 seconds before sending the next ICMP packet
        time.sleep(2)

if __name__ == "__main__":
    main()

    # End
    
    #ChatGPT was refenced for this code
