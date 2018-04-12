from PathLinker import *
from XmlLoader import *
from LanIpIdentifier import *
from DNSFinder import *


# Get the file that we want to parse from the user.
filepath = input("Please enter the xml file name that you want to parse: ")

# Parse the file.
packets = Parse(filepath)

# Retrieve Chun's IP
ip = GetChunsLanIP(packets)

# Display it to the user.
print("Chun's LAN IP on this file is: " + str(ip))

# Initializing hashtable.
initHashtable(filepath)

print(ipToDNS("52.207.61.132"))
