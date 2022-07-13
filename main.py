def solution():
    ip = input("Enter your IP Address in the form (x.x.x.x/x):")

    x = ip
    octets = []
    for i in range(0, 3):
        x = x.partition("."[0])
        octets.append(int(x[0]))
        x = x[2]
    x = x.partition("/"[0])
    octets.append(int(x[0]))
    octets.append(int(x[2]))

    first_octet = octets[0]
    second_octet = octets[1]
    fourth_octet = octets[3]

    # Class A
    if 0 <= first_octet <= 127:
        if first_octet == 10:
            print("Output: Class: A, Designation: Private")
        elif first_octet == 127 and 1 <= fourth_octet <= 255:
            print("Output: Class: A, Designation: Special")
        else:
            print("Output: Class: A, Designation: Public")

    # Class B
    if 128 <= first_octet <= 191:
        if (first_octet == 171) and (16 <= second_octet <= 31):
            print("Output: Class: B, Designation: Private")
        elif (first_octet == 169) and (second_octet == 254):
            print("Output: Class: B, Designation: Automatic Private IP Addressing (APIPA)")
        else:
            print("Output: Class: B, Designation: Public")

    # Class C
    if 192 <= first_octet <= 223:
        if (first_octet == 192) and (second_octet == 168):
            print("Output: Class: C, Designation: Private")
        else:
            print("Output: Class: C, Designation: Public")

    # Class D
    if 224 <= first_octet <= 239:
        print("Output: Class: D")

    # Class E
    if 240 <= first_octet <= 255:
        print("Output: Class: E")


if __name__ == '__main__':
    solution()
