import os
import socket

print("=== NETWORK DIAGNOSTIC TOOL ===")

# Check internet connectivity
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Internet Status: Connected")
    except OSError:
        print("Internet Status: Not Connected")

# Ping Google
def ping_test():
    print("\nRunning Ping Test...")
    response = os.system("ping -n 4 google.com")  # For Windows
    if response == 0:
        print("Ping Status: Success")
    else:
        print("Ping Status: Failed")

check_internet()
ping_test()
