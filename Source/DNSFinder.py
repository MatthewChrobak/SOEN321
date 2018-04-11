# Initialize hashtable

def initHashtable(filepath):
    global Hashtable
    filepath = filepath + ".txt"

    # Initialize the hashtable as empty
    Hashtable = {}
    
    # Opening the file and read the lines of it
    with open(filepath) as filestream:
        lines = filestream.readlines()
        
        # Loop through the lines that contains ip and dns
        # And split them by a tab
        for i in range(6, len(lines)):
            line = lines[i]
            lineData = line.split("\t")

            # Just to be clear c:
            ip = lineData[0]
            dnsValue = lineData[1]

            # Add the ip and dns pair into the hashtable
            Hashtable.update({ ip : dnsValue })

            

def ipToDNS(ip):
    # Make sure the IP exists in the hashtable.
    if (ip in Hashtable):
        return Hashtable[i]

    # Otherwise, return Null / None
    return None
