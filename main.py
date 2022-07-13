while True:

    try:

        IP = str(input("Please enter the IP address: "))
        numslice = IP.split('.')

        #Octet 1,2 slicer
        q1 = int(numslice[0])
        q2 = int(numslice[1])
    
        #Binary slicing 
        SubnetMask = IP.split('/')
        SubnetMask_Index = SubnetMask[1]
        Octet = ('.'.join([bin(int(x)+256)[3:] for x in SubnetMask[0].split('.')]))
    
        print("............................")
        print("IP Address:",IP)
        print("Binary:",Octet)
        print("Subnet Mask:",SubnetMask_Index)
        

        def Class_And_IP_Type(): 
            #Identifying The Class Type  
            
            if Octet[0] == '0': 
                print("Class A") 

            elif Octet[:2] == '10': 
                print("Class B") 

            elif Octet[:3] == '110': 
                print("Class C") 

            elif Octet[:4] == '1110': 
                print("Class D") 

            elif Octet[:4] == '1111': 
                print("Class E") 

            #Determining The IP Type

            if q1 == 10:
                print("Private IP Address")
            elif q1 == 172 and q2 >= 16 and q2 <= 31:
                print("Private IP Address")
            elif q1 == 192 and q2 == 168:
                print("Private IP Address")
            elif q1 == 127:
                print("Special IP Adress")
            else:
                print("Public IP Address")
   


        if __name__ == '__main__':  
            Class_And_IP_Type()
            
        exit()
    except (IndexError,ValueError,TypeError):
        print("Please Enter A Valid Input")
    
