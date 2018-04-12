from PathLinker import *
from XmlLoader import *
from LanIpIdentifier import *


# Get the file that we want to parse from the user.
filepath = input("Please enter the xml file name that you want to parse: ")

# Parse the file.
packets = Parse(filepath)

# Retrieve Chun's IP
ip = GetChunsLanIP(packets)

# Display it to the user.
print("Chun's LAN IP on this file is: " + str(ip))

AllSources = AllSources(packets)

print(AllSources)

''' For searching individual users
otherIP = GetOtherLanIP(packets)

print("\nThese are the other IPs on this file: " + str(otherIP))

user = input("\nWhich user would you like to look at: ")

sources = GetSourceIP(user, packets)

'''
