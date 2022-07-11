def solution(ip):
    ip=ip.split(".")
    ip=[int(i) for i in ip]
    if(ip[0]>=0 and ip[0]<=127):
        nc="A"
    elif(ip[0]>=128 and ip[0]<=191):
        nc="B"
    elif(ip[0]>=192 and ip[0]<=223):
        nc="C"
    elif(ip[0]>=224 and ip[0]<=239):
        nc="D"
    elif(ip[0]>=240 and ip[0]<=255):
        nc="E"
    else:
        print("This number is not ip ...")
        
    if(nc=="A"):
        if(ip[0]==10):
            de="Private"
        elif(ip[0]==127 and ip[3]>=1):
            de="Special"
        else:
            de="Public"
    elif(nc=="B"):
        if(ip[0]==172 and(ip[1]>=16 and ip[1]<=31)):
            de="Private"
        else:
            de="Public"
    elif(nc=="C"):
        if(ip[0]==192 and ip[1]==198):
            de="Private"
        else:
            de="Public"
    elif(nc=="D" or nc=="E"):
        de="Public"

    print("Class: ",nc," , Designation: ",de)


if __name__ == '__main__':
    ip=input("Enter the IP Address :")
    solution(ip)
