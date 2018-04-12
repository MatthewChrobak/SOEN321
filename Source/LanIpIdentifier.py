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
