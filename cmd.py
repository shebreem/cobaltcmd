import os
import socket
import time

def get_ip_address(website):
    try:
        hostname = socket.gethostbyname(website)
        return hostname
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def run_command(command):
    try:
        os.system(command)
    except Exception as e:
        print(f"Error occurred while running command: {e}")

def process_command():
    command = input("You: ")
    if "webip" in command:
        website = input("Enter the website: ")
        ip_address = get_ip_address(website)
        if ip_address:
            print(f"IP Address for {website}: {ip_address}")
    else:
        run_command(command)

while True:
    print("Welcome to the cobalt terminal")
    process_command()
    time.sleep(1)
