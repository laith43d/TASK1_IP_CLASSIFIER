import sys
print(sys.argv)

def ipcalclator():
    ipaddress = sys.argv[1]
    ip = ipaddress.split("/")[0].split(".")

    " Class A "

    if int(ip[0]) == 127 and 0 <= int(ip[1]) <= 255:
        print('The Class of your IP is A and Designation is Special')
    elif 1 <= int(ip[0]) <= 126:
        if int(ip[0]) == 10:
            print('The Class of your IP is A and Designation is Private')

        else:
            print('The Class of your IP is A and Designation is  Public')

            " Class B "

    elif 128 <= int(ip[0]) <= 191:
        if ((int(ip[0]) == 172) and (16 <= int(ip[1]) <= 31)) or ((int(ip[0]) == 169) and (int(ip[1]) == 254)):
            print('The Class of your IP is B and Designation is Private')
        else:
            print('The Class of your IP is B and Designation is Public')

            " Class C "

    elif 192 <= int(ip[0]) <= 223:
        if int(ip[0]) == 192 and (int(ip[1]) == 168):
            print('The Class of your IP is C and Designation is Private')
        else:
            print('The Class of your IP is C and Designation is Public')

            " Class D "

    elif 224 <= int(ip[0]) <= 239:
        print('The Class of your IP is D and Designation is Special')

        " Class E "

    elif 240 <= int(ip[0]) <= 255:
        print('The Class of your IP is E and Designation is Special')
    else:
        print("Enter your IP in form of x.x.x.x/x")


if __name__ == '__main__':
    if len(sys.argv) > 1:
     ipcalclator()
    else:
     print(input("Enter your IP in form of x.x.x.x/x"))
else:
    print(input("Enter your IP in form of x.x.x.x/x"))
