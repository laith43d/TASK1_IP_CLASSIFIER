import sys
ip = (sys.argv[1]).split('.')

# function to get class type and designation
def solution(part1 , part2): 

    #class type
    if int(part1) in range(0, 128):
        class_Type = "A"
    elif int(part1) in range(128, 192):
        class_Type = "B"
    elif int(part1) in range(192, 224):
        class_Type = "C"
    elif int(part1) in range(224, 240):
        class_Type = "D"
    elif int(part1) in range(240, 256):
        class_Type = "E"

    #designation
    if (int(part1) == 10 ) or (int(part1) == 172 and int(part2) in range(16, 32)) or (int(part1) == 192 and int(part2) == 168) :
        designation = "Praivate"
    elif int(part1) == 127 :
        designation = "Special"
    else: 
        designation = "Public"

    return class_Type , designation
    
if __name__ == '__main__':

#input validation
    try:
        ip_oc1 = int(ip[0])
        ip_oc2 = int(ip[1])
        ip_oc3 = int(ip[2])
        ip_oc4 = int(ip[3])

        #check ip range
        if len(ip) == 4 and (ip_oc1 in range(0, 256)) and (ip_oc2 in range(0, 256)) and (ip_oc3 in range(0, 256)) and (ip_oc4 in range(0, 256)):
            check_ip_range = True    
        
            #assign the return values to variables
            class_type, designation = solution(ip_oc1, ip_oc2)

            #print the output
            if check_ip_range == True:
                print("Class: " + class_type +", "+ "Designation: " + designation)
            else:
                print("Unvalid IP address")
        else:
            print("Unvalid IP address")

    except ValueError:
        print("Unvalid IP address")