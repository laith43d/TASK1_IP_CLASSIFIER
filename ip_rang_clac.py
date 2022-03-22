

from tokenize import String
from xmlrpc.client import Boolean


def find_ip_range(ip_add):
    if ip_add >=1 and (ip_add) <=127:

        return 'A'

    elif (ip_add) >=128 and (ip_add) <=191:
        return 'B'

    elif (ip_add) >=192 and (ip_add) <=223:
        return 'C'

    # elif (ip_add) >= 224 and  (ip_add) <=239:
    #     return 'D'

    # elif (ip_add) >=240 and  (ip_add)<=255:
    #     return'E'

    else:
        return '1'


def find_desginateA(ip_address : list) -> String:
    if ip_address[0]==10:
        return 'private'
    elif ip_address[0]==172 and (ip_address[1] >=16 and ip_address[1] <=31) :
        return 'private'
    elif ip_address[0]==169 and (ip_address[1] ==254) :
        return 'private'
    elif ip_address[0]==192 and (ip_address[1] ==168) :
        return 'private'
    else:
        return 'public'


# def find_desginateB (ip_address : list) -> String:
#     if ip_address[0]==172 and (ip_address[1] >=16 and ip_address[1] <=31) :
#         return 'private'
#     elif ip_address[0]==169 and (ip_address[1] ==254) :
#         return 'private'
#     else:
#         return 'public'



# def find_desginateC (ip_address : list) -> String:
#     if ip_address[0]==192 and (ip_address[1] ==168) :
#         return 'private'

#     else:
#         return 'public'




def check_if_special(ip_address : list) -> Boolean:
    if ip_address[0]==127:
        if ip_address[1]==0 and ip_address[2] ==0 and  ip_address[3]==0:
            #only 127.0.0.0 is public
            return 'Class: A, Designation: Public'
        else:
            return 'Class: A, Designation: Special'

    elif ip_address[0] >= 224 and  ip_address[0] <=239:
        return 'Class: D, Designation: Special'

    elif ip_address[0]>=240 and   ip_address[0] <=255:
        return 'Class: E, Designation: Special'

    else:
        return '0'

   