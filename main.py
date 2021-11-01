import sys


def solution():
    full_ip = sys.argv[1]
    ip = full_ip.split("/")[0]
    ip = ip.split(".")
    if int(ip[0]) == 127 and 0 <= int(ip[1]) <= 255:
        print('Class A, Designation: Special')
    elif 1 <= int(ip[0]) <= 126:
        if int(ip[0]) == 10:
            print('Class A, Designation: private')
        else:
            print('Class A, Designation: public')
    elif 128 <= int(ip[0]) <= 191:
        if ((int(ip[0]) == 172) and (16 <= int(ip[1]) <= 31)) or ((int(ip[0]) == 169) and (int(ip[1]) == 254)):
            print('Class B, Designation: private')
        else:
            print('Class B, Designation: public')
    elif 192 <= int(ip[0]) <= 223:
        if int(ip[0]) == 192 and (int(ip[1]) == 168):
            print('Class C, Designation: private')
        else:
            print('Class C, Designation: public')
    elif 224 <= int(ip[0]) <= 239:
        print('Class D,Designation: Special')
    elif 240 <= int(ip[0]) <= 255:
        print('Class E, Designation: Special')
    else:
        print("enter the ip in form of x.x.x.x/x")


if __name__ == '__main__':
    solution()
else:
    print("enter the ip in form of x.x.x.x/x")
