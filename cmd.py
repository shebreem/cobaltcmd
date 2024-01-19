import os
import socket
import time
import requests
import random
import sys


os.system("title cobalt labs")
text_to_print = """
                     __                  __    __            __         __   
                    /  |                /  |  /  |          /  |      _/  |  
  _______   ______  $$ |____    ______  $$ | _$$ |_         $$ |____ / $$ |  
 /       | /      \ $$      \  /      \ $$ |/ $$   |        $$      \$$$$ |  
/$$$$$$$/ /$$$$$$  |$$$$$$$  | $$$$$$  |$$ |$$$$$$/         $$$$$$$  | $$ |  
$$ |      $$ |  $$ |$$ |  $$ | /    $$ |$$ |  $$ | __       $$ |  $$ | $$ |  
$$ \_____ $$ \__$$ |$$ |__$$ |/$$$$$$$ |$$ |  $$ |/  |      $$ |__$$ |_$$ |_ 
$$       |$$    $$/ $$    $$/ $$    $$ |$$ |  $$  $$/       $$    $$// $$   |
 $$$$$$$/  $$$$$$/  $$$$$$$/   $$$$$$$/ $$/    $$$$/        $$$$$$$/ $$$$$$/ 
                                                                          
                                                                             
                                                                                                  
"""

print(text_3)
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
def list_time_zones():
    print("""
    Samoa: -11
    Hawaii: -10
    Alaska: -9
    Pacific Time (US & Canada): -8
    Mountain Time (US & Canada): -7
    Central Time (US & Canada): -6
    Eastern Time (US & Canada): -5
    Brasilia: -3
    Greenland: -3
    Cape Verde: -1
    Azores: -1
    England: 0
    GMT (Greenwich Mean Time): 0
    Western European Time: 0
    Central European Time: +1
    Eastern European Time: +2
    Moscow Time: +3
    Iran Time: +3:30
    India Standard Time: +5:30
    Japan Standard Time: +9
    Australian Eastern Time: +10
    New Zealand Standard Time: +12""")
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
    elif "timezones" in command:
        list_time_zones()
    elif "yo" in command or "hello" in command:
        print("Hello! How can I help you?")
    elif "exit" in command:
        os.system(exit)
    else:
        run_command(command)

while True:
    process_command()
