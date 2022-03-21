import ip_rang_clac


def solution():
    my_ip=input('Enter Ip Address in the following format : x.x.x.x/x')
    print (my_ip)

    ip_address=my_ip[0:my_ip.index('/')]
    list_ip_address=ip_address.split('.')
    new_int_iplist=[int (i) for i in list_ip_address ]
   
# first, check if the IP is special

    res=ip_rang_clac.check_if_special(new_int_iplist) 
    if res !='0':
        print(res)
    else:
        first_oct=new_int_iplist[0]
        rang=ip_rang_clac.find_ip_range(int(first_oct))
        print ('Class : ',rang,', Designation : ',ip_rang_clac.find_desginateA(new_int_iplist))


if __name__ == '__main__':
    solution()
