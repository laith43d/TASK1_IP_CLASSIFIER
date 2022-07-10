ip = str(input("Please enter the ip address: "))
numslice = ip.split('.')
q1 = int(numslice[0])
q2 = int(numslice[1])
SubnetMask = ip.split('/')
SubnetMask_Index = SubnetMask[1]
Octet = ('.'.join([bin(int(x)+256)[3:] for x in SubnetMask[0].split('.')]))
print("IP Address:",ip)
print("Binary:",Octet)
print("Subnet Mask:",SubnetMask_Index)

def Class_And_IP_Type(): 
      #identifying the class type  
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
    #determining the ip type
    
    if q1 == 10:
        print("Private IP Address")
    elif q1 == 172 and q2 >= 16 and q2 <= 31:
        print("Private IP Address")
    elif q1 == 192 and q2 == 168:
        print("Private IP Address")
    elif q1 == 127:
        print("Special IP Adress")
    elif q1 == 169:
        print("Special IP Adress")
    else:
        print("Public IP Address")
    
    
    return(Result)    



if __name__ == '__main__':  
    print("Class: "+Class_And_IP_Type())
