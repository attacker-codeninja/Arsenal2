# Network Discovery Script

This Bash script facilitates network exploration by identifying network ranges, discovering IP addresses, and performing host pings within a specified domain.

# Usage

Clone the Repository:

    git clone https://github.com/Vulnpire/network-discovery.git

# Run the Script:

    ./discovery.sh <domain>

Replace <domain> with the target domain you want to explore.

# Functionality

Upon execution, the script identifies the IP addresses associated with the specified domain.
It offers the following options:
Identify Network Range: Obtain the network range for discovered IP addresses.
Ping Discovered Hosts: Ping the identified hosts to check their availability.
All Checks: Perform both network range identification and host pings.
Exit: Terminate the script.

# Note
This script relies on external commands like whois, prips, and ping, so ensure they are installed and accessible in your environment.
