import json


def view_ips():
    # Load existing data
    try:
        with open('ips.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # Print out each IP and its associated time
    for ip, time in data.items():
        print(f"IP: {ip}, Time: {time}")


view_ips()
