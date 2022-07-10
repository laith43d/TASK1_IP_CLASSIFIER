def solution(ip):
    ip = ip.split("/")[0].split(".")
    # ip validation
    if len(ip) != 4 :print("ip is not correct");exit()
    try:
        part1, part2, part3, part4 = int(ip[0]), int(ip[1]), int(ip[2]),int(ip[3])
    except ValueError:
        print("ip is not correct")
        exit()
    if ((part1 or part2 or part3 or part4) not in range(0,256)):
        print("Please check if the ip is in range")
        exit()
    # boolean values
    publicA = part1 in range(0,128)
    publicB = part1 in range(128,192)
    publicC = part1 in range(192,224)
    publicD = part1 in range(224,240)

    privateA = part1 == 10
    privateB = part1 == 172 and part2 in range(16,32)
    privateC = part1 == 192 and part2 == 168

    special = part1 == 127 and part4 != 0

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