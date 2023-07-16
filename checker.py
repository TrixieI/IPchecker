import json
import datetime


def clean_ips():
    # Load existing data
    try:
        with open('ips.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # Get current date
    current_date = datetime.datetime.now()

    # Check each IP
    for ip, date in list(data.items()):
        date_of_entry = datetime.datetime.fromisoformat(date)
        # If the IP has been there for more than 90 days, remove it
        if (current_date - date_of_entry).days > 90:
            del data[ip]

    # Write data back to the file
    with open('ips.json', 'w') as f:
        json.dump(data, f)


clean_ips()
