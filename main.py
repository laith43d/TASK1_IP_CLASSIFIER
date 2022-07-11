from ipaddress import ip_address
def solution():
    pass 
#The user input ip like 192.168.0.1/24
ip = input("Input the ip/mask and enter : ")

#The string splits at this specified separator('/') between ip and mask
ip = ip.split('/') # The ip located before ('/') 1
mask = ip[1] # The mask located after (/) 1
ipAddress = ip[0].split('.') # ip[0] = The ip before (/) split ('.') four like (192.168.0.1)


# Function of Class type and Set public, private or private
def solution(ipAddress):
    
    if int(ipAddress[0]) in range(0,128) and int(mask) in range(8,32): #If the first term is (0 to 128) this is class A
        classType = 'A'
        classError = False
    elif int(ipAddress[0]) in range(128,192)and int(mask) in range(8,32):#If the first term is (128 to 192) this is class B
        classType = 'B'
        classError = False
    elif int(ipAddress[0]) in range(192, 224)and int(mask) in range(8,32):#If the first term is (192 to 224) this is class C
        classType = 'C'
        classError = False
    elif int(ipAddress[0]) in range(224, 240)and int(mask) in range(8,32):#If the first term is (224 to 240) this is class D
        classType = 'D'
        classError = False
    elif int(ipAddress[0]) in range(240, 255)and int(mask) in range(8,32):#If the first term is (240 to 255) this is class E
        classType = 'E'
        classError = False
    else:
        classType = ''
        classError = True
        
   # Set public, private or private
   # if the first range == 10 in mask (8,32) or 172 and  Second range of 172 is 16 or 31 in mask (8,32) or first range = 192 and Second range of 192 = 168  in mask (8,32) ===== Private
    if (int(ipAddress[0]) ==10 and int(mask) in range(8,32)) or (int(ipAddress[0]) == 172 and int(ipAddress[1]) in range(16,31) and int(mask) in range(8,32)) or (int(ipAddress[0]) == 192 and int(ipAddress[1]) == 168 and int(mask) in range(8,32)):
        setType = 'Private'
        # if first range = 127 and four range = 1 or 255 in mask = 8  ==== Special
    elif int(ipAddress[0]) == 127 and int(mask) in range(8,32) and int(ipAddress[3]) in range(1,255) :
        setType = 'Special'
        # other is Public
    elif int(mask) in range(8,32):
        setType = 'Public'
    else:
        setType = ''
        classError = True
        
        
    return classType , setType , classError


if __name__ =='__main__':
    pass 
     #Here to assign or specify and return the values of variables
    classType , setType , classError  = solution(ipAddress)
     
    x=0
    while x < len(ipAddress):
        if int(ipAddress[x]) in range(0,255):
            ipRange = True
        else:
            ipRange = False
        x+=1
    if ipRange == True:
        if classError == True:
            print("Invalid IP address")
        elif classError ==False:
         print("Output: Class: "+ classType +"\nDesignation " + setType)
         
            
