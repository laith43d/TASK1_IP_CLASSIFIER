
import sys

IP_with_mask=(sys.argv[1]).split('/')


def solution(IP_1,IP_2): 
    
    #For Public IP Address
    if IP_1>=1 and IP_1<=9 or IP_1>=11 and IP_1<=126 :
        IP_Class="A"
        IP_Type="public"
    elif IP_1>=128 and IP_1<=191:
        IP_Class="B"
        IP_Type="public"
    elif IP_1>=192 and IP_1<=223:
        IP_Class="C"
        IP_Type="public"

    #For Private IP Address
    if IP_1==10 :
        IP_Class="A"
        IP_Type="Private"
    elif IP_1==169 and IP_2==254:
        IP_Class="B"
        IP_Type="Private APIPA"
    elif IP_1==172 and 16<= IP_2 <=31 :
        IP_Class="B"
        IP_Type="Private"
    elif IP_1==192 and IP_2==168:
        IP_Class="C"
        IP_Type="Private"


    #For Special IP Address
    if IP_1==127:
        IP_Class="A"
        IP_Type="Special"
    elif IP_1>=224 and IP_1<=239:
        IP_Class="D"
        IP_Type="Special"
    elif IP_1>=240 and IP_1<=255:
        IP_Class="E"
        IP_Type="Special"
    
    #PRINT OUTPUT
    print("Class :" + IP_Class ,", Descignation :" + IP_Type)
if __name__ == '__main__':
    IP=IP_with_mask[0].split('.')
    #INPUT ECCEPTANCE TEST
    try:
        IP1=int(IP[0])
        IP2=int(IP[1])
        IP3=int(IP[2])
        IP4=int(IP[3])
        print(type(IP1))
        if len(IP)==4 and (IP1 in range(0,256)) and (IP2 in range(0,256)) and (IP3 in range(0,256)) and (IP4 in range(0,256)):
            solution(IP1,IP2)
        else:
            print("OUT OF THE RANGE...")
    except ValueError:
        print("Unvalid IP address...")