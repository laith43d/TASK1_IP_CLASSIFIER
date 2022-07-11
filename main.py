def solution():
    ip_address = input('enter your ip address: ')
    ip_test = ip_address.split('.')
    if ip_test[0]== '10':
        Class = "A"
        designation = "private"
    elif ip_test[0]== '127':
        Class = "A"
        designation = "special"    
    elif ip_test[0]== "172" and 16<=ip_test[0]<=31 :
        Class = "B"
        designation = "private"   
    elif ip_test[0]== "192" and ip_test[1]== "168":
        Class = "C"
        designation = "private"     
    elif ip_test[0]>1 and ip_test[0]<127:
        Class = "A"
        designation = "public"  
    elif ip_test[0]>128 and ip_test[0]<192 :
        Class = "B"
        designation = "public"    
    elif ip_test[0]>192 and ip_test[0]<224 :
        Class = "C"
        designation = "public"    
    elif ip_test[0]>224 and ip_test[0]<240 :
        Class = "D"
        designation = "public"        
    elif ip_test[0]>240 and ip_test[0]<255 :
        Class = "class: E" 
        designation = "reserved"     
    else:
        raise ValueError
    print (f'class: {Class} , designation: {designation}')
if __name__ == '__main__':
    solution()

