#user input
ip = input("Enter IP/Mask : ")

#split the ip address and mask
ip= ip.split('/')
mask = ip[1]
ip_address = ip[0].split('.')

# function to get class type and designation
def solution(ip_address):
    #class type
    if int(ip_address[0]) in range(0, 128):
        class_Type = "A"
    elif int(ip_address[0]) in range(128, 192):
        class_Type = "B"
    elif int(ip_address[0]) in range(192, 224):
        class_Type = "C"
    elif int(ip_address[0]) in range(224, 240):
        class_Type = "D"
    elif int(ip_address[0]) in range(240, 256):
        class_Type = "E"
    

    #designation
    if (int(ip_address[0]) == 10 ) or (int(ip_address[0]) == 172 and int(ip_address[1]) in range(16, 32)) or (int(ip_address[0]) == 192 and int(ip_address[1]) == 168) :
        designation = "Praivate"
    elif int(ip_address[0]) == 127 and int(ip_address[3]) in range(1, 256):
        designation = "Special"
    else: 
        designation = "Public"

    return class_Type , designation



if __name__ == '__main__':

    # assign the returns values to variables
    class_type, designation = solution(ip_address)


    #check the validation of the ip
    i=0
    while i < len(ip_address):
        if int(ip_address[i]) in range(0, 256) :
            check_ip_range = True
        else:
            check_ip_range = False
        i+=1
    
    
    #print the output
    if check_ip_range == True:
        print("Class: " + class_type +", "+ "Designation: " + designation)
    else:
        print("Unvalid IP address")

