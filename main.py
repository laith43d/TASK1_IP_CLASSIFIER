import sys, re


def solution():
    str
    ipv4 = (
        "(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])");
    if (not (1 < len(sys.argv) < 3 and re.match(ipv4, sys.argv[1]))):
        print('enter correct input: x.x.x.x\\x')
        return

    octas = sys.argv[1].split(".")
    if 1 <= int(octas[0]) <= 127:
        if int(octas[0]) == 10:
            print('Class A, Designation: private')
        else:
            print('Class A, Designation: public')

    elif 128 <= int(octas[0]) <= 191:
        if int(octas[0]) == 127 and (16 <= int(octas[1]) <= 31):
            print('Class B, Designation: private')
        elif int(octas[0]) == 169 and (int(octas[1]) == 254):
            print('Class B, Designation: private')
        elif int(octas[0]) == 127:
            print('Class B, Designation: Special')
        else:
            print('Class B, Designation: public')

    elif 192 <= int(octas[0]) <= 223:
        if int(octas[0]) == 192 and (int(octas[1]) == 168):
            print('Class C, Designation: private')
        else:
            print('Class C, Designation: public')

    elif 224 <= int(octas[0]) <= 239:
        print('Class D,Designation: multicast')

    elif 240 <= int(octas[0]) <= 254:
        print('Class E, Designation: reserved')


if __name__ == '__main__':
    solution()
