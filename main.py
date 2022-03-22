str = input("enter the IP address :")
    str = str.split('.')
    #ip CLASS A,B,C,D,E
    if int(str[0]) >=1 and int(str[0]) <=127 : print("Output: Class A", end = ' ')
    elif int(str[0]) >= 128 and int(str[0]) <= 191: print("Output: Class B", end = ' ')
    elif int(str[0]) >= 192 and int(str[0]) <= 223: print("Output: Class C", end = ' ')
    elif int(str[0]) >= 224 and int(str[0]) <= 239: print("Output: Class D", end = ' ')
    elif int(str[0]) >= 240 and int(str[0]) <= 255: print("Output: Class E", end = ' ')
    else :print("error input")

    #Private and Special Ip address
    if int(str[0]) == 10 and (int(str[1]) >= 0 and int(str[1])<=255):
        print ("Designation: private")
    elif int(str[0]) == 172 and (int(str[1]) >= 16 and int(str[1])<=31):
        print ("Designation: private")
    elif int(str[0]) == 192 and (int(str[1]) == 168):
        print ("Designation: Private")
    elif int(str[0]) == 127 :
        print ("Designation: Special")
    else :
        print("Designation: Public")
    #the subnet mask
    subnet = (str[-1])
    subnet =subnet.split("/")



if name == 'main':
    x = Solution()
    print("the subnet mask = "+x.subnet[1])
