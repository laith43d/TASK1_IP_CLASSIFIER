
def solution(): #Function

    #For Public IP Address
    if IP_Address[0]>=1 and IP_Address[0]<=9 or IP_Address[0]>=11 and IP_Address[0]<=126 :
        IP_Class="A"
        IP_Type="public"
    elif IP_Address[0]>=128 and IP_Address[0]<=191:
        IP_Class="B"
        IP_Type="public"
    elif IP_Address[0]>=192 and IP_Address[1]< 168 and IP_Address[0]<=223:
        IP_Class="C"
        IP_Type="public"

    #For Private IP Address
    if IP_Address[0]==10 :
        IP_Class="A"
        IP_Type="Private"
    elif IP_Address[0]==169 and IP_Address[0]==254:
        IP_Class="B"
        IP_Type="Private APIPA"
    elif IP_Address[0]==172 and 16<= IP_Address[1] <=31 :
        IP_Class="B"
        IP_Type="Private"
    elif IP_Address[0]==192 and IP_Address[1]==168:
        IP_Class="C"
        IP_Type="Private"

    #For Special IP Address
    if IP_Address[0]==127:
        IP_Class="A"
        IP_Type="Special"
    elif IP_Address[0]>=224 and IP_Address[0]<=239:
        IP_Class="D"
        IP_Type="Special"
    elif IP_Address[0]>=240 and IP_Address[0]<=255:
        IP_Class="E"
        IP_Type="Special"

    
    print("Class: "+IP_Class ,"Descintion: "+IP_Type)

if __name__ == '__main__':
    IP=input("Enter Your IP Address, In This Way IP/MASK: ")
    IP_Mask=IP.split('/')
    IP_Address=IP_Mask[0].split('.')

    try:
        IP_Address=[int(i) for i in IP_Address]
    except ValueError as e:
        print(e)

    if IP_Address[0]>=1 and IP_Address[0]<=256:
            solution()
    else:
            print("OUT OF THE RANGE....")
