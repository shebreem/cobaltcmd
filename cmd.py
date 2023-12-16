import socket
import time

def get_ip_address(website):
    try:
        hostname = socket.gethostbyname(website)
        return hostname
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def command():
    com = input("You: ")
    if "webip" in com:
        website = input("Enter the website: ")
        ip_address = get_ip_address(website)
        if ip_address:
            print(f"IP Address for {website}: {ip_address}")

while True:
    print("Welcome to the cobalt terminal")
    command()
    time.sleep(1)
