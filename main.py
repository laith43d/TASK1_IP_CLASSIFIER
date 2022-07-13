def solution():
    pass


def solution(ip):
    listip = ip.split("/")
    iparray = listip[0].split(".")


    n1 = (int(iparray[0]))
    n2 = (int(iparray[1]))
    n3 = (int(iparray[2]))
    n4 = (int(iparray[3]))
    n5 = (int(listip[1]))

    if n1 in range(0, 128) and n2 in range(0, 256) and n3 in range(0, 256) and n4 in range(0, 256) and n5 == 24 and n1 !=10:
        print("this is 'public' ip Class A")

    elif n1 == 10 and n2 in range(0, 256) and n3 in range(0, 256) and n4 in range(0, 256)and n5 == 24:
        print("this is 'private' ip Class A")

    elif n1 in range(128, 192) and n2 in range(0, 256) and n3 in range(0, 256) and n4 in range(0, 256) and n5 == 24:
        print("this is 'public' ip Class B")

    elif n1 == 172 and n2 in range(16,32) and n3 in range(0, 256) and n4 in range(0, 256) and n5 == 24:
     print("this is 'private' ip Class: B")

    elif n1==169 and n2==254 and n3 in range(0, 256) and n4 in range(0, 256) and n5 == 24:
     print("this is 'private APIPA ' ip Class B ")

    elif n1 in range(192, 223) and n2 in range(0, 256) and n3 in range(0, 256) and n4 in range(0, 256) and n5 == 24:
        print("this is 'public' ip Class C")

    elif n1 ==192 and n2 == 168 and n3 in range(0, 256) and n4 in range(0, 256) and n5 == 24:
        print("this is 'private' ip Class C")

    elif n1 in range(224, 240) and n2 in range(0, 256) and n3 in range(0, 256) and n4 in range(0, 256) and n5 == 24:
        print("this ip in Class D")

    elif n1 in range(240, 256) and n2 in range(0, 256) and n3 in range(0, 256) and n4 in range(0, 256) and n5 == 24:
        print("this ip in Class E")



    elif n2 or n3 or n4 < 0 and n2 or n3 or n4 > 255:
     print("The ip out of range try again!!!!!!!")


    elif n1 < 0 or n1 > 255:
     print("The ip out of range try again!!!!!!!")

    elif n5 !=24:
        print("chic your Subnet Mask")

    else:print("it is special ip")

if __name__ == '__main__':
    pass
ip = input("enter the ip:")


solution(ip)
