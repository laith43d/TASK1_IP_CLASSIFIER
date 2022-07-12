
def solution():
    pass
#IP input
    IP = str(input('Enter IP:'))

#Listing and Splting the IP
    IP_1 = list(IP.split('/')) 

#Take every thing befor the (/)    
    IP_2 = IP_1[0]

#Listing and Spliting evry thing befor the (/)
    IPtoList = list(IP_2.split('.'))
    
#Converting String to int
    IP_inx_1 = (int(IPtoList[0]))
    IP_inx_2 = (int(IPtoList[1]))
    IP_inx_3 = (int(IPtoList[2]))
    IP_inx_4 = (int(IPtoList[3]))

#chcking evry thing working with print
    print(IPtoList)
    print(IP_inx_1)
    print(IP_inx_2)
    print(IP_inx_3)
    print(IP_inx_4)

#testing the IP for it's Class and Designation
    if IP_inx_1 in range(1,128) and IP_inx_2 == 0 and IP_inx_3 == 0 and IP_inx_4 == 0:
        print('IP class: A and Designation: Public')

    elif IP_inx_1 == 10 and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
        print('IP class: A and Designation: Private')

    elif IP_inx_1 in range(128,192) and IP_inx_2 in range(0,256) and IP_inx_3 == 0 and IP_inx_4 == 0:
        print('IP class: B and Designation: Public')

    elif IP_inx_1 == 127 and IP_inx_2 in range(16,32) and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
        print('IP class: B and Designation: Privet')

    elif IP_inx_1 in range(192,224) and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 == 0:
        print('IP class: C and Designation: Public')

    elif IP_inx_1 == 192 and IP_inx_2 == 168 and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
        print('IP class: C and Designation: Privet')

    elif IP_inx_1 in range(224,240) and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
        print('IP class: D')

    elif IP_inx_1 in range(240,256) and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
        print('IP class: E')

    elif IP_inx_1 == 127 and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 in range(1,256):
        print('IP class : A and Designation: Special')
    else:
        print('You entered a wroing IP')



if __name__ == '__main__':
    pass

solution()
