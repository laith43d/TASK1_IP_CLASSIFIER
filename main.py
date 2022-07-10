def solution(ip):
    ip = ip.split("/")[0].split(".")
    # ip validation
    if len(ip) != 4 :print("ip is not correct");exit()
    try:
        A, B, C, D = int(ip[0]), int(ip[1]), int(ip[2]),int(ip[3])
    except ValueError:
        print("ip is not correct")
        exit()
    if ((A or B or C or D) not in range(0,256)):
        print("Please check if the ip is in range")
        exit()
    # boolean values
    publicA = A in range(0,128)
    publicB = A in range(128,192)
    publicC = A in range(192,224)
    publicD = A in range(224,240)

    privateA = A == 10
    privateB = A == 172 and B in range(16,32)
    privateC = A == 192 and B == 168

    special = A == 127 and D != 0

    # check type
    if special:print("class A special")
    elif privateA:print("class A Private")
    elif privateB:print("class B Private")
    elif privateC:print("class C Private")
    elif publicA:print("class A Public")
    elif publicB:print("class B Public")
    elif publicC:print("class C Public")
    elif publicD:print("class D Public")
    else:print("Class E Public")
    
if __name__ == '__main__':
    solution(input())