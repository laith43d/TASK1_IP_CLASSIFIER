ip = str(input("Please enter the ip address: "))
numslice = ip.split('.')

#Octet 1,2 slicer
q1 = int(numslice[0])
q2 = int(numslice[1])

#Octet 4 slicer 
q4slice = numslice[3].split('/')
q4slice2 = q4slice[0].split('.')
q4=int(q4slice2[0])

#Binary slicing 
SubnetMask = ip.split('/')
SubnetMask_Index = SubnetMask[1]
Octet = ('.'.join([bin(int(x)+256)[3:] for x in SubnetMask[0].split('.')]))

print("IP Address:",ip)
print("Binary:",Octet)
print("Subnet Mask:",SubnetMask_Index)

def Class_And_IP_Type(): 
    #Identifying the class type  
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

    #Determining the IP type

    if q1 == 10:
        print("Private IP Address")
    elif q1 == 172 and q2 >= 16 and q2 <= 31:
        print("Private IP Address")
    elif q1 == 192 and q2 == 168:
        print("Private IP Address")
    elif q1 == 127 and q4 >=1 and q4<=255:
        print("Special IP Adress")
    else:
        print("Public IP Address")


    return(Result)    


if __name__ == '__main__':  
    print("Class: "+Class_And_IP_Type())
