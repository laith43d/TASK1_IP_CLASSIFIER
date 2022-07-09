def solution(ip):
    ip2 = ip
    
    x = ip3 = 0
    for i in  range(len(ip)): 
        if ip[i] == '.':
            x = i
            # ip3 = int (ip2[x +1 : x+ 4])
            ip =int( ip[0:x])
            #class A
            if ip > 0  and ip < 128 :
                print("IP address class (A)")
                if ip == 10 : 
                    print("IP address designation (Private)")
                else :
                    print("IP address designation (Public)")
            elif ip >= 128 and ip < 191 : 
                #class B
                print("IP address class (B)")
                if ip == 172 : 
                    print("IP address designation (Private)")
                else :
                    print("IP address designation (Public)")
            elif ip >= 192 and ip < 223 : 
                #class c
                print("IP address class (C)")
                h = len(ip2)
                if h == 11 :
                    ip3 = int (ip2[x +1 : x+ 4])
                if ip3  == 168: 
                    print("IP address designation (Private)")
                else :
                    print("IP address designation (Public)")
            elif ip >= 224  and ip <= 239 :
                print("IP address class (D)")
            else: 
                print("IP address class (E)")
            break
        





if __name__ == '__main__':
    ip = input("Enter Your Ip Address: ")
    solution(ip)
