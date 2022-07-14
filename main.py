
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
    IP_inx_4 = (int(IPtoList[3]))

#testing the IP for it's Class and Designation
    
    if IP_inx_1 == 127 and IP_inx_4 == 1:
        print('IP class : A and Designation: Special')
    
    elif IP_inx_1 == 10:
        print('IP class: A and Designation: Private')
    
    elif IP_inx_1 in range(1,128):
        print('IP class: A and Designation: Public')

    elif IP_inx_1 == 172 and IP_inx_2 in range(16,32):
        print('IP class: B and Designation: Privet')

    elif IP_inx_1 in range(128,192):
        print('IP class: B and Designation: Public')

    elif IP_inx_1 == 192 and IP_inx_2 == 168:
        print('IP class: C and Designation: Privet')

    elif IP_inx_1 in range(192,224):
        print('IP class: C and Designation: Public')

    elif IP_inx_1 in range(224,240):
        print('IP class: D')

    elif IP_inx_1 in range(240,256):
        print('IP class: E')
    
    else:
         print('You entered an invaled IP, Try again'),solution()
        


if __name__ == '__main__':
    pass

solution()
