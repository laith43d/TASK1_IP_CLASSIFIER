def solution():
    pass

ip = str(input("enter ip address: "))
numofslice = ip.split('.')

SubnetMask = ip.split('/')
SubnetMask_Index = SubnetMask[1]
Octet = ('.'.join([bin(int(x)+256)[3:] for x in SubnetMask[0].split('.')]))




s1 = int(numofslice[0])
s2 = int(numofslice[1])

if __name__ == '__main__':
    pass

slice1 = numofslice[3].split('/')
slice2 = slice1[0].split('.')
s4=int(slice2[0])




print("IP Address:",ip)

def IP_Type(): 
    
    Result = '' 
    if Octet[0] == '0': 
        Result = 'A' 

    elif Octet[:2] == '10': 
        Result = 'B' 

    elif Octet[:3] == '110': 
        Result =  'C' 

    elif Octet[:4] == '1110': 
        Result = 'D' 

    elif Octet[:4] == '1111': 
        Result = 'E' 

   

    if s1 == 10:
        print("Designation:Private IP Address")
    elif s1 == 172 and s2 >= 16 and s2 <= 31:
        print("Designation:Private IP Address")
    elif s1 == 192 and s2 == 168:
        print("Designation:Private IP Address")
    elif s1 == 127 and s4 >=1 and s4<=255:
        print("Designation:Special IP Adress")
    else:
        print("Designation:Public IP Address")


    return(Result)    


if __name__ == '__main__':  
    print("Class: "+IP_Type())
