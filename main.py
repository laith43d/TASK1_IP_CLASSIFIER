import sys


def solution():
    ip = (sys.argv[1].split("/"))
    octet = ip[0].split(".")
    if 1 <= int(octet[0]) <= 127:
        if int(octet[0]) == 10:
            print('Class: A, Designation: private')
        else:
            print('Class: A, Designation: public')

    elif 128 <= int(octet[0]) <= 191:
        if int(octet[0]) == 127 and (16 <= int(octet[1]) <= 31):
            print('Class: B, Designation: private')
        elif int(octet[0]) == 169 and (int(octet[1]) == 254):
            print('Class: B, Designation: private')
        elif int(octet[0]) == 127:
            print('Class: B, Designation: Special')
        else:
            print('Class: B, Designation: public')

    elif 192 <= int(octet[0]) <= 223:
        if int(octet[0]) == 192 and (int(octet[1]) == 168):
            print('Class: C, Designation: private')
        else:
            print('Class: C, Designation: public')

    elif 224 <= int(octet[0]) <= 239:
        print('Class: D,Designation: Special')

    elif 240 <= int(octet[0]) <= 254:
        print('Class: E, Designation: Special')


if __name__ == '__main__':
    solution()
