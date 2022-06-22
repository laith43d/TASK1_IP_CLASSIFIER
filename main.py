import re
from sys import argv


def solution():
    ipClass = ""
    ipDesignation = ""
    print(argv[1])
    input = argv[1]
    ipList = re.split("[/ .]", input)
    ip = [int(x) for x in ipList[0:4]]


# or (len(max(ipList[0:4])) > 3
#                             or len(min(ipList[0:4])) < 1

    if len(ipList) != 5 or not any([x.isnumeric() for x in ipList]):
        print("Wrong Input, the entered IP should look like this (123.123.123.123/123)")

    elif (int(max(ipList[0:4])) > 255 or int(min(ipList[0:4])) < 0):
        print("Wrong Input the range of IP sections should be from 0 to 255")
    else:
        print(ipList)

        if (ip[0] >= 1 and ip[0] <= 127):
            ipClass = "A"
            ipDesignation = "Public"
            if ip[0] == 10:
                ipDesignation = "Private"
            else:
                ipDesignation = "Special"

        elif (ip[0] >= 128 and ip[0] <= 191):
            ipClass = "B"
            ipDesignation = "Public"
            if ip[0] == 172 and (ip[1] >= 16 and ip[1] <= 31):
                ipDesignation = "Private"

        elif (ip[0] >= 192 and ip[0] <= 223):
            ipClass = "C"

            if ip[0] == 192 and ip[1] == 168:
                ipDesignation = "Private"
            elif ip[3] == 0:
                ipDesignation = "Public"
            else:
                ipDesignation = "Special"

        elif ip[0] >= 224 and ip[0] <= 239:
            ipClass = "D"
            ipDesignation = "Special"

        elif ip[0] >= 240:
            ipClass = "E"
            ipDesignation = "Special"

    print("Output: Class: ", ipClass, ", Designation: ", ipDesignation)


if __name__ == '__main__':
    solution()
