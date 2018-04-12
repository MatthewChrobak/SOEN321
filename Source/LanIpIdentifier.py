# This module is in charge of identifying Chun's IP address on the
# local area network.

from XmlLoader import GetProperty

MacAddress = "Apple_c4:8c:97"


def GetChunsLanIP(parseData):
    # Get all the packets from the parse.
    packets = parseData["packet"]


    # Loop through all the packets and return the destination address
    # of the packet whose protocol is TCP and whose destination MAC address
    # matches Chun's MAC address.
    for i in range(0, len(packets)):
        packet = packets[i]
        if (GetProperty(packet, "Destination MAC") == MacAddress and GetProperty(packet, "Protocol") == "TCP"):
            return GetProperty(packet, "Destination")

#To get a list of all users and all the sources
def AllSources(parseData):
    packets = parseData["packet"]
    listOfIp=[]

    for i in range(0, len(packets)):
        packet = packets[i]
        ip = str(GetProperty(packet, "Destination"))

        if ip.startswith('192.168') and GetProperty(packet, "Destination MAC") != MacAddress \
                and not GetProperty(packet, "Destination") in listOfIp and GetProperty(packet, "Protocol")=="TCP":
            listOfIp.append(GetProperty(packet, "Destination"))
            print('\n-------------------------------------------------------------')
            print("\nFetching all sources linked to IP address: {} \n" .format(GetProperty(packet, "Destination")) )
            listofSources=[]

            for j in range(0, len(packets)):
                packet = packets[j]

                if GetProperty(packet, "Destination") == ip and not GetProperty(packet, "Source") in listofSources \
                        and GetProperty(packet, "Destination MAC") != MacAddress and GetProperty(packet, "Protocol")=="TCP":
                    listofSources.append(GetProperty(packet, "Source"))
                    print(GetProperty(packet, "Source"))

''' For looking at an individual user
def GetOtherLanIP(parseData):
    packets = parseData["packet"]
    listOfIP = []

    #Loops through all the packets and returns a list of LanIPs that are not Chun's
    for i in range(0, len(packets)):
        packet=packets[i]
        ip=str(GetProperty(packet, "Destination"))

        #Matches IP addresses that start with 192.168 and adds them to the list a single time
        if ip.startswith('192.168') and GetProperty(packet, "Destination MAC") != MacAddress \
                and not GetProperty(packet, "Destination") in listOfIP and GetProperty(packet, "Protocol")=="TCP":

            listOfIP.append(GetProperty(packet,"Destination"))

    return listOfIP

#For getting a list of sources from an individual user
def GetSourceIP(DestIP, parseData):
    packets = parseData["packet"]
    listofSources=[]

    for i in range(0, len(packets)):
        packet=packets[i]

        if GetProperty(packet, "Destination")==DestIP and not GetProperty(packet, "Source") in listofSources \
                and GetProperty(packet, "Protocol") == "TCP":
            listofSources.append(GetProperty(packet, "Source"))
            print(GetProperty(packet, "Source"))
'''