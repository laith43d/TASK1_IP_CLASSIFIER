def solution():
    pass 

    ip_list=ip.split('.')
    last_octet=ip_list[-1].split('/')
    ip_address=""
    if len(ip_list)==4 and last_octet[0]!='' :
        ip_list[-1]=last_octet[0]
        try :    
            for index,value in enumerate(ip_list) :
                ip_list[index]=int(value)
            if ip_list[0]>=1 and ip_list[0]<=127:
                if ip_list[1]<0 or ip_list[2]<0 or ip_list[3]<0 :
                    print("Unvalid Ip Address")
                elif ip_list[1]>255 or ip_list[2]>255 or ip_list[3]>255 :
                    print("Unvalid Ip Address")
                else :    
                    ip_address="A"
                    if ip_list[0]==10:
                        if ip_list[1]!=0 or ip_list[2]!=0 or ip_list[3] != 0 :
                            ip_address_designation="Private"
                        else :
                            ip_address_designation="Public"
                    elif ip_list[0]==127 :
                        if ip_list[1]!=0 or ip_list[2]!=0 or ip_list[3] !=0 :
                            ip_address="A"
                            ip_address_designation="Special"
                        else :
                            ip_address="A"
                            ip_address_designation="Public"
                    else :
                        ip_address_designation="Public"                 
            elif ip_list[0] >=128 and ip_list[0]<=191 :
                if ip_list[1]<0 or ip_list[2]<0 or ip_list[3]<0 :
                    print("Unvalid Ip Address")
                elif ip_list[1]>255 or ip_list[2]>255 or ip_list[3]>255 :
                    print("Unvalid Ip Address")
                else:    
                    ip_address="B"
                    if ip_list[0]==172 :
                        if ip_list[1]>=16 and ip_list[2]<=31 :
                            ip_address_designation="Private"
                        else :
                            ip_address_designation="Public"
                    else :
                        ip_address_designation="Public"
            elif ip_list[0]>=192 and ip_list[1]<=223 :
                if ip_list[1]<0 or ip_list[2]<0 or ip_list[3]<0 :
                    print("Unvalid Ip Address")
                elif ip_list[1]>255 or ip_list[2]>255 or ip_list[3]>255 :
                    print("Unvalid Ip Address") 
                else :       
                    if ip_list[1]<0 or ip_list[2]<0 or ip_list[3]<0 :
                        print("Unvalid Ip Address")
                    elif ip_list[1]>255 or ip_list[2]>255 or ip_list[3]>255 :
                        print("Unvalid Ip Address")    
                    else:
                        ip_address="C"
                        if ip_list[0]==192 and ip_list[1]==168 :
                            ip_address_designation="Private"

                        else :
                            ip_address_designation="Public"    
                        
            elif ip_list[0]>=224 and ip_list[0]<=239:
                if ip_list[1]<0 or ip_list[2]<0 or ip_list[3]<0 :
                    print("Unvalid Ip Address")
                elif ip_list[1]>255 or ip_list[2]>255 or ip_list[3]>255 :
                    print("Unvalid Ip Address")
                else :    
                    ip_address="D"
                    ip_address_designation="Special"
            elif ip_list[0]>=240 and ip_list[0]<=255:
                if ip_list[1]<0 or ip_list[2]<0 or ip_list[3]<0 :
                    print("Unvalid Ip Address")
                elif ip_list[1]>255 or ip_list[2]>255 or ip_list[3]>255 :
                    print("Unvalid Ip Address")
                else:
                    ip_address="E"
                    ip_address_designation="Special"    
                
            else:
                print("Unvalid Ip Address")

            if ip_address!="":
                print("Your Ip Address Class is :" + ip_address)
                print("Your Ip Address Designation is :" + ip_address_designation)    
        except :
            print("Unvalid Ip Address")
    else :
        print('Unvalid Ip Address')    

ip=input("enter a valid ip address for example (192.12.14.0/24)")


   

if __name__ == '__main__':
    pass
