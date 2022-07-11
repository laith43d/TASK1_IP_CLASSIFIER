def solution():
    ip_address = input('enter your ip address: ')
    ip = ip_address.split('/')
    ip_test = ip[0].split('.')

    part1 = int(ip_test[0])
    part2 = int(ip_test[1])
    part3 = int(ip_test[2])
    part4 = int(ip_test[3])
    if part1== 10:
        Class = "A"
        designation = "private"
    elif part1== 127  and 1<=part4<=255 :
        Class = "A"
        designation = "special"    
    elif part1== 172 and 16<=part1<=31 :
        Class = "B"
        designation = "private"   
    elif part1== 192 and part2== 168:
        Class = "C"
        designation = "private"     
    elif part1>=1 and part1<=127:
        Class = "A"
        designation = "public"  
    elif part1>=128 and part1<=192 :
        Class = "B"
        designation = "public"    
    elif part1>=192 and part1<=224 :
        Class = "C"
        designation = "public"    
    elif part1>=224 and part1<=240 :
        Class = "D"
        designation = "public"        
    elif part1>=240 and part1<=255 :
        Class = "class: E" 
        designation = "reserved"     
    else:
        raise ValueError
    print (f'class: {Class} , designation: {designation}')
if __name__ == '__main__':
    solution()
