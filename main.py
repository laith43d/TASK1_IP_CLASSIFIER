def solution():
    IP=input("Enter ip adress /Netmask :")
    IP_LIST=IP.split('.')
    oct1=int(IP_LIST[0])
    oct2=int(IP_LIST[1])
    oct3=int(IP_LIST[2])
    oct4=int(IP_LIST[3].split('/')[0])
    #netmask=int(IP_LIST[3].split('/')[1])
    bin1=bin(int(oct1))
    print(bin1)
    bin1=str(bin1[2::])
    bin1=bin1.zfill(8)
    count=0

    for i in bin1:
        if i == '0':
             break
        count += 1
    if count==0:
        Class='A'
        if oct1==10:
            state="private"
        elif(oct1 ==100 and oct2 in range(64,127+1)):
            state="special"
        else:
            state="public"
    elif count==1:
        Class='B'
        #public
        #129.0.0.0 - 169.253.255.255
        #169.255.0.0 - 172.15.255.255
        #172.32.0.0 - 191.0.1.255
        #private
        #172.16.0.0-172.31.255.255
        if ((oct1 in range(130,168+1) ) or
                (oct1 ==129) or
                (oct1 ==169 and oct2 in range(0,253)) or
            (oct1 in range(170,171+1) ) or
            (oct1 == 169 and oct2==255) or
            (oct1 == 172 and oct2 in range(0,15+1)) or
            (oct1 in range(173,191+1)) or
            (oct1 ==172 and oct2 in range(32,255+1)) or
            (oct1==191 and oct2 ==0 and oct3 in range(0,1+1))):
            state="public"
        elif oct1 == 172 and oct2 in range(16, 31+1):
            state="private"
        else:
            state="special"
    elif count==2:
        Class='C'
        #public
        #192.0.3.0 - 192.88.98.255
        #192.88.100.0 - 192.167.255.255
        #192.169.0.0 - 198.17.255.255
        #198.20.0.0 - 223.255.255.255
        #private
        #192.168.0.0-192.168.255.255
        if(oct1==192 and oct2 in range(0,88+1) and oct3 in range(3,98+1) or
          (oct1==192 and oct2 in range(88,167+1) and oct3 in range(100,255+1)) or
                (oct1==192 and oct2 in range(169,255+1)) or
                (oct1 in range(193,197+1)) or
                (oct1 ==198) and oct2 in range(0,17+1) or
                    (oct1==198 and oct2 in range(20,255+1)) or
                (oct1 in range(199,233+1))):
            state="public"
        elif(oct1==192 and oct2==168):
            state="private"
        else:
            state="speical"

    elif count==3:
        Class='D'
    elif count==4:
        Class='E'
    else:
        Class="undifined"
        state="special"
    print(Class)
    print(state)
if __name__ == '__main__':
    solution()
