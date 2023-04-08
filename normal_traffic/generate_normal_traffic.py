import random
import time
import requests

# Replace this list with your own list of allowed server addresses
SERVER_ADDRESSES = [
    "http://youtube.com", "http://github.com", "http://chess.com", "http://slidesdaddy.com"
]

while True:
    # Pick a random server address
    server_address = random.choice(SERVER_ADDRESSES)
    print(f"Connecting to: {server_address}")

    # Send an HTTP GET request
    try:
        response = requests.get(server_address)
        if response.status_code == 200:
            print("Successful")
    except requests.RequestException as e:
        print(f"Error: {e}")

    # Random delay between requests (1 to 5 seconds)
    time.sleep(random.randint(1, 5))
