def solution():
 
    IP_address = input("enter the  IP address : ")
    classIP=IP_address.split(".")
    IP_address_one=int(classIP[0])
    IP_address_Second = int(classIP[1])

    if IP_address_one in range(0,128):
        if IP_address_one==10:
            print("Class:A, Designation: public")
        elif 1>=IP_address_one<=126 and IP_address_one !=10:
            print("Class: A, Designation: Special")
        elif IP_address_one==127:
            print("Class: A, Designation: Special")


    elif IP_address_one in range(128,192):
        if IP_address_one == 127 and 16 <= IP_address_Second <= 31:
            print("Class:B, Designation: Private")
        elif IP_address_one == 169 and IP_address_Second == 254:
            print('Class: B, Designation: private')
        elif IP_address_one == 127:
            print('Class: B, Designation: Special')
        else:print('Class: B, Designation: public')


    elif IP_address_one in range(192,224):
        if IP_address_one== 192 and IP_address_Second == 168:
            print('Class: C, Designation: private')
        elif 224 <= IP_address_one<= 239:
            print('Class: C,Designation: Special')
        else:
            print('Class: C, Designation: public')


    elif IP_address_one in range(224,240):
        print('Class: D,Designation: Special')

    elif IP_address_one in range(240,256):
        print('Class: E, Designation: Special')




if __name__ == '__main__':
    solution()
