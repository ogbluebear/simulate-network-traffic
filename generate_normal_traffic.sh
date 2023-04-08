#!/bin/bash

# Replace this list with your own list of allowed server addresses if you want
SERVER_ADDRESSES=("http://youtube.com" "http://github.com" "http://chess.com" "http://slidesdaddy.com")

while true; do
    # Pick a random server address
    server_address=${SERVER_ADDRESSES[$RANDOM % ${#SERVER_ADDRESSES[@]}]}
    echo "Connecting to: $server_address"

    # Send an HTTP GET request using curl
    wget -q -O /dev/null "$server_address"

    # Random delay between requests (1 to 5 seconds)
    sleep $((RANDOM % 5 + 1))
done