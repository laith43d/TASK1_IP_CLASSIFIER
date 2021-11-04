"""
Class A:
Public IP Range: 1.0.0.0 to 127.0.0.0
Private IP Range: 10.0.0.0 to 10.255.255.255

Class B:
Public IP Range: 128.0.0.0 to 191.255.0.0
Private IP Range: 172.16.0.0 to 172.31.255.255

Class C:
Public IP Range: 192.0.0.0 to 223.255.255.0
Private IP Range: 192.168.0.0 to 192.168.255.255

Class D:
Range: 224.0.0.0 to 239.255.255.255

Class E:
Range: 240.0.0.0 to 255.255.255.255
"""


import sys


class Solution:
    ClassIP = ""
    Designation = ""

    def __init__(self, input_ip):

        self.ipInput = input_ip
        self.subNet = input_ip[input_ip.find("/") + 1::]

        # checking if octet value is > 255 or equals zero!

        for octet in input_ip:
            if int(octet) > 255 and int(octet) == 0:
                print("Error, please try again!")

        # octet value
        self.octet1 = int(input_ip[0])
        self.octet2 = int(input_ip[1])
        self.octet3 = int(input_ip[2])
        self.octet4 = int(input_ip[3])

    def recognize_ip(self):

        # Class A
        if 0 <= self.octet1 <= 127:
            self.ClassIP = "A"
            # Designation
            if self.octet1 == 10:
                self.Designation = "Private"
            elif self.octet1 == 127 and self.octet4 >= 1:
                self.Designation = "Special"
            else:
                self.Designation = "Public"

        # Class B
        elif 128 <= self.octet1 <= 191:
            self.ClassIP = "B"
            # Designation
            if self.octet1 == 172 and 16 <= self.octet2 <= 32:
                self.Designation = "Private"
            else:
                self.Designation = "Public"

        # Class C
        elif 192 <= self.octet1 <= 223:
            self.ClassIP = "C"

            # Designation
            if self.octet1 == 192 and self.octet2 == 168:
                self.Designation = "Private"
            else:
                self.Designation = "Public"

        # Class D
        elif 224 <= self.octet1 <= 239:
            self.ClassIP = "D"
            self.Designation = "(There's no Designation for class D)"

        # Class E
        elif 240 <= self.octet1 <= 255:
            self.ClassIP = "E"
            self.Designation = "(There's no Designation for class E)"

        self.recognize_ip()
        return f'Class : {self.ClassIP}, Designation : {self.Designation}'


if __name__ == '__main__':
    print(Solution(sys.argv[1]))
