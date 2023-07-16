import json


def remove_ips():
    # Load existing data
    try:
        with open('ips.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # Ask for IPs
    ips = input("Please enter IPs to remove, separated by spaces or commas: ")

    # Split the input string into separate IPs
    ips = ips.replace(',', ' ').split()

    # Remove each IP
    for ip in ips:
        if ip in data:
            del data[ip]

    # Write data back to the file
    with open('ips.json', 'w') as f:
        json.dump(data, f)


remove_ips()
