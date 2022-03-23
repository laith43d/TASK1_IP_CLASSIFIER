import sys
import ip_rang_clac


def solution():
    my_ip=input('Enter Ip Address in the following format : x.x.x.x/x')
    
    print (my_ip)

    new_int_iplist =[]
    digit_flag,new_int_iplist=validity(my_ip)
    
    # first, check if the IP is special
    if digit_flag:
        res=ip_rang_clac.check_if_special(new_int_iplist) 
        if res !='0':
            print(res)
        else:
            first_oct=new_int_iplist[0]
            rang=ip_rang_clac.find_ip_range(int(first_oct))
            print ('Class : ',rang,', Designation : ',ip_rang_clac.find_desginateA(new_int_iplist))
    else:
        sys.exit(1)






def validity(my_ip):
    try:
        ip_address=my_ip[0:my_ip.index('/')]
        list_ip_address=ip_address.split('.')
        new_int_iplist=[int (i) for i in list_ip_address ]
         # check if the user enters 4 digit only
        if len(new_int_iplist)==4:
            for item in new_int_iplist:
                if 0 <= item <=255:
                    digit_flag=True
                else:
                    print('Please Enter the Ip in correct format x.x.x.x/x , and each digit is between 0 and 255')
                    digit_flag=False
                    break
            return digit_flag,new_int_iplist
        
        else:
            print('Please Enter the Ip in the following correcting format x.x.x.x/x that consists of 4 digits and subnet mask ')
            sys.exit(1)
    except ValueError:
        print("Enter Ip address in the following correcting format x.x.x.x/x that conatins numbers only (4-digits) and backslash ")
        sys.exit(1)
    
   







if __name__ == '__main__':
  
    solution()

