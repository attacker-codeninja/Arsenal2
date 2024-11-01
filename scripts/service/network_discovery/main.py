#!/bin/bash

# Function to handle interruption
function cleanup {
    echo -e "\n\e[1;31mExiting...\e[0m"
    exit 1
}
trap cleanup INT

# Check for given arguments
if [ $# -eq 0 ]
then
        echo -e "\e[1;33mYou need to specify the target domain.\e[0m\n"
        echo -e "Usage:"
        echo -e "\t$0 <domain>"
        exit 1
else
        domain=$1
fi

# Identify Network range for the specified IP address(es)
function network_range {
        for ip in $ipaddr
        do
                netrange=$(whois $ip | grep "NetRange\|CIDR" | tee -a CIDR.txt)
                cidr=$(whois $ip | grep "CIDR" | awk '{print $2}')
                cidr_ips=$(prips $cidr)
                echo -e "\n\e[1;34mNetRange for $ip:\e[0m"
                echo -e "$netrange"
        done
}

# Ping discovered IP address(es)
function ping_host {
        hosts_up=0
        hosts_total=0

        echo -e "\n\e[1;34mPinging host(s):\e[0m"
        for host in $cidr_ips
        do
                stat=1
                while [ $stat -eq 1 ]
                do
                        ping -c 2 $host > /dev/null 2>&1
                        if [ $? -eq 0 ]
                        then
                                echo -e "\e[1;32m$host is up.\e[0m"
                                ((stat--))
                                ((hosts_up++))
                                ((hosts_total++))
                        else
                                echo -e "\e[1;31m$host is down.\e[0m"
                                ((stat--))
                                ((hosts_total++))
                        fi
                done
        done

        echo -e "\n\e[1;32m$hosts_up out of $hosts_total hosts are up.\e[0m"
}

# Identify IP address of the specified domain
hosts=$(host $domain | grep "has address" | cut -d" " -f4 | tee discovered_hosts.txt)

echo -e "\e[1;34mDiscovered IP address:\e[0m\n$hosts\n"
ipaddr=$(host $domain | grep "has address" | cut -d" " -f4 | tr "\n" " ")

# Available options
echo -e "\e[1;36mAdditional options available:\e[0m"
echo -e "\t\e[1;33m1) Identify the corresponding network range of target domain.\e[0m"
echo -e "\t\e[1;33m2) Ping discovered hosts.\e[0m"
echo -e "\t\e[1;33m3) All checks.\e[0m"
echo -e "\t\e[1;33m*) Exit.\e[0m\n"

read -p "Select your option: " opt

case $opt in
        "1") network_range ;;
        "2") ping_host ;;
        "3") network_range && ping_host ;;
        "*") exit 0 ;;
esac
