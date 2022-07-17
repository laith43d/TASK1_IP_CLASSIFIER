
from ipaddress import ip_address

def solution (ip_address):
    ip =ip_address.split(".")
    a=int(ip[0])
    b=int(ip[1])
    c=int(ip[2])
    d=int(ip[3])
    if a in range(1,128) and (0 <=int(b)<=255)and \
        (0 <= int(c) <=255) and \
            (1<= int(d)<=255):
        print("class A ,Special") 
    elif a==10 and (0 <=int(b) <=255 ):
        print("Class A ,Private")
    elif a in range (1,128):
        print("class A,public")

    elif a==169 and b ==254 and \
        (0<= int(c)<=255) and (0<=int(d)<=255):
         print ("Class B,Apipa")
    elif a==172 and (31 <=int(b) <=16 ):
         print("Class B ,Private")
    elif 128<=int(a)<=191:
         print("class B,public")

    elif a==192 and b==168:
        print("Class C ,Private") 

    elif 192<=int(a)<=223:
         print("class C,public")

    elif 224<=int(a)<=239:
         print("class D")
 
    elif 240<=int(a)<=255:
         print("class E")

    else:
        print ("Ip Address is incorrect")


if __name__=='__main__':
    input ="170.30.0.0"
    solution(input)
