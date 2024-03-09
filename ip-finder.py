import socket
import subprocess

def ping_website(ip_address):
    try:
        subprocess.run(["ping", ip_address])
    except KeyboardInterrupt:
        print("\nPing aborted by user.")

try:
    print('''\033[32m
    _         _____ _           _           
   (_)_ __   |  ___(_)_ __   __| | ___ _ __ 
   | | '_ \  | |_  | | '_ \ / _` |/ _ \ '__|
   | | |_) | |  _| | | | | | (_| |  __/ |   
   |_| .__/  |_|   |_|_| |_|\__,_|\___|_|   
     |_|
                                    by linux        
\033[0m''')
    website = input("Enter the website URL(www.Example.com):-")
    ip_address = socket.gethostbyname(website)
    print(f"The ip address of Website is:{ip_address}")

    ping_option = input("Do you want to ping the website? (yes/no):-").lower()
    
    if ping_option == "yes":
        ping_website(ip_address)
    elif ping_option != "no":
        print("Skipping ping")

except socket.gaierror:
    print("Error: Invalid website URL or website is not reachable")
except KeyboardInterrupt:
    print("\nOpertion aborted by user")                            
