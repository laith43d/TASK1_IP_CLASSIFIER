def solution():
    pass
def solution(ip):
    listip=ip.split("/")
    iparray=listip[0].split(".")

    n1=(int(iparray[0]))
    n2 = (int(iparray[1]))
    n3 = (int(iparray[2]))
    n4 = (int(iparray[3]))
    n5 = (int(listip[1]))


    if n1 in range(1,127) and n2 in range(0,255) and n3 in range(0,255) and n4 in range(0,255) and n5 ==24:
        print("this is 'public' ip Class A")

    elif n1 ==10 and n2 in range(0, 255) and n3 in range(0, 255) and n4 in range(0, 255) and n5 == 24:
            print("this is 'privat' ip Class A")

    elif n1 in range(128, 191) and n2 in range(0, 255) and n3 in range(0, 255) and n4 in range(0, 255) and n5 == 24:
                print("this is 'public' ip Class B")

    elif n1 == 172 and n2 in range(0, 255) and n3 in range(0, 255) and n4 in range(0, 255) and n5 == 24:
        print("this is 'privat' ip Class: B")


    elif n1 or n2 or n3 or n4 <1 and n1 or n2 or n3 or n4 >255:
        print("The ip out of range try again!!!!!!!")

    elif n5 !=24:
        print("chic your Subnet Mask")

    else:print("it is special ip")

if __name__ == '__main__':
    pass
ip=input("enter the ip:")
solution(ip)
