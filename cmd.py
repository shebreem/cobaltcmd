import os
import socket
import time
import requests
import random
import sys


os.system("title cobalt labs")
text_to_print = """            ___.          .__   __   
    ..____  ____\_ |__ _____  |  |_/  |_
    _/ ___\/  _ \| __ \\__  \ |  |\   __|
    \  \__(  <_> ) \_\ \/ __ \|  |_|  |  
    .\___  >____/|___  (____  /____/__|  
    ......\/          \/     \/            
"""
print(text_to_print)
print("Welcome to the cobalt terminal")

def get_location_from_ip(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

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
            location_data = get_location_from_ip(ip_address)
            if location_data:
                print(f"Location: {location_data['city']}, {location_data['regionName']}, {location_data['country']}")
    elif "locip" in command:
        ip_address = input("Enter the IP address: ")
        location_data = get_location_from_ip(ip_address)
        if location_data:
            print(f"Location for {ip_address}: {location_data['city']}, {location_data['regionName']}, {location_data['country']}")
    elif "weather" in command:
        countrynshi = str(input("what place are you in mate: "))
        awdas = ("curl wttr.in" + "/" + countrynshi)
        os.system(awdas)
    elif "pick" in command:
    # Get a list of items from the user
        items_input = input("Enter a list of items separated by commas: ")
        items_list = items_input.split(',')
        try:
            # Pick a random item from the list
            choice = random.choice(items_list)
            print(choice)
        except IndexError:
            print("The list is empty. Please enter some items.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif "yo" in command or "hello" in command:
        print("Hello! How can I help you?")
    elif "exit" in command:
        os.system(exit)
    else:
        run_command(command)

while True:
    process_command()
