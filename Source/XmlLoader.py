# This module is in charge of loading the
# PSML file into a dictionary object containing its information.

import xmltodict

def Parse(filename):
    global WiresharkProperties

    # Feedback for the user c: These files are big and can take some time.
    print("Parsing the data...")
    
    try:
        with open(filename) as filestream:
            obj = xmltodict.parse(filestream.read())

            # More feedback for the user.
            print("Done parsing.")

            # Assign the column data for later parsing use.
            WiresharkProperties = obj["psml"]["structure"]["section"]

            # The root object is psml.
            return obj["psml"]

        
    except IOError as e:
        print("Had an issue parsing the file " + filename + ": " + e)


def GetProperty(packet, propertyName):
    propertyIndex = WiresharkProperties.index(propertyName)

    # Return None if the property doesn't exist.
    if (propertyIndex == -1):
        print("The property " + propertyName + " doesn't exist.")
        print("We only have " + WiresharkProperties)
        return None
    
    return packet['section'][propertyIndex]
