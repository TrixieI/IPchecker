import json
import datetime


def insert_ips():
    # Load existing data
    try:
        with open('ips.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # Ask for IPs
    ips = input("Please enter IPs, separated by spaces or commas: ")

    # Split the input string into separate IPs
    ips = ips.replace(',', ' ').split()

    # Insert each IP with the current date
    for ip in ips:
        # Only add the IP if it's not already in the data
        if ip not in data:
            data[ip] = datetime.datetime.now().isoformat()

    # Write data back to the file
    with open('ips.json', 'w') as f:
        json.dump(data, f)


insert_ips()
