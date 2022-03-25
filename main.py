def solution():
    ip_address = input("enter your IP adress: x.x.x.x/x ")
    ip_mask =  ip_address.split("/")
    ip_class = ip_mask[0].split('.')
     
    
    if 1 <= int(ip_class[0]) <= 127:
        if int(ip_class[0]) == 10:
            print('Class: A, Designation: private')
        else:
            print('Class: A, Designation: public')

    elif 128 <= int(ip_class[0]) <= 191:
        if int(ip_class[0]) == 127 and (16 <= int(ip_class[1]) <= 31):
            print('Class: B, Designation: private')
        elif int(ip_class[0]) == 169 and (int(ip_class[0]) == 254):
            print('Class: B, Designation: private')
        elif int(ip_class[0]) == 127:
            print('Class: B, Designation: Special')
        else:
            print('Class: B, Designation: public')

    elif 192 <= int(ip_class[0]) <= 223:
        if int(ip_class[0]) == 192 and (int(ip_class[1]) == 168):
            print('Class: C, Designation: private')
        else:
            print('Class: C, Designation: public')

    elif 224 <= int(ip_class[0]) <= 239:
        print('Class: D,Designation: Special')

    elif 240 <= int(ip_class[0]) <= 254:
        print('Class: E, Designation: Special')


if __name__ == '__main__':
    solution()

