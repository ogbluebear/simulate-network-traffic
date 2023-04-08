## Network Attack Scripts for Windows, Linux, and MacOS
Scripts for simulating various network attacks using shell/python
Some functionalities from .sh scripts that are often available on Linux and MacOS aren't available on Windows, so there are alternative python scripts

# Generating Normal Network traffic

## How to use on Linux/MacOS machine:

Must have wget installed
Wget comes with most linux machines, but you might need to install it for MacOs - https://www.cyberciti.biz/faq/howto-install-wget-om-mac-os-x-mountain-lion-mavericks-snow-leopard/

1. clone the repository:

git clone https://github.com/williamnamgyal/network-attack-scripts

2. change directory:

cd network-attack-scripts

3. make script executable:

chmod +x generate_normal_traffic.sh

4. run the script:

./generate_normal_traffic.sh

## How to use on Windows machines
For Windows machines, there are 2 options: the generate_normal_traffic.sh file or generate_normal_traffic.py file
If you do not have Git bash, you won't be able to run .sh files on windows, so I recommend using generate_normal_traffic.py

1. clone the repository:

git clone https://github.com/williamnamgyal/network-attack-scripts

2. change directory:

cd network-attack-scripts

3. install required libraries:
pip install requests

4. run the script:

python generate_normal_traffic.py
