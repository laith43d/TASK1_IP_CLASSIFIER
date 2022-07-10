def solution(): #Function
    #Enter IP From User
    IP=input("Enter IP address,writ it in this style IP/MASK:") 
    print(IP)
    #Class Ranges and Designation Types
    if IP>="1.0.0.0" and IP<="127.0.0.0":#For Class A (Public)
     IP_Class="A"
     IP_Type="Public"
     if IP>="10.0.0.0" and IP<="10.255.255.255":#For Class A (Private)
        IP_Class="A"
        IP_Type="Private"
    elif IP>="128.0.0.0" and IP<="191.255.0.0":#For Class B (Public)
     IP_Class="B"
     IP_Type="Public"
     if IP>="172.16.0.0" and IP<="172.31.255.255":#For Class B (Private)
        IP_Class="B"
        IP_Type="Private"
    elif IP>="192.0.0.0" and  IP<="223.255.255.0":#For Class C (Public)
     IP_Class="C"
     IP_Type="Public"
    elif IP>="192.168.0.0" and IP<="192.168.255.255":#For Class C (Private)
        IP_Class="B"
        IP_Type="Private"
    elif IP>="127.0.0.1" and IP<="127.255.255.255":#For Class C (Special)
        IP_Class="B"
        IP_Type="Special"
    elif IP>="224.0.0.0" and IP<="239.255.255.255":#For Class D (Public)
     IP_Class="D"
     IP_Type="Public"
    elif IP>="240.0.0.0" and IP<="255.255.255.255":#For Class E (Public)
     IP_Class="E"
     IP_Type="Public"
    print("Class: "+IP_Class +", Designation:" +IP_Type) #Print OutPut,The Class's type and Designation's type that the user has entered

if __name__ == '__main__':
     solution() #Call The Function
