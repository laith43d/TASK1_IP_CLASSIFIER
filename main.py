def solution():
    print("Please Enter an Ip adress: " , end='')
    ip = input()
    ip = ip.split("/")[0].split(".")
    # ip validation
    if len(ip) != 4 :print("ip is not correct\n");solution()
    try:
        part1, part2, part3, part4 = int(ip[0]), int(ip[1]), int(ip[2]),int(ip[3])
    except ValueError:
        print("ip is not correct\n")
        solution()
    if ((part1 or part2 or part3 or part4) not in range(0,256)):
        print("Please check if the ip is in range\n")
        solution()
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
    if special:print("Class: A, Designation: Special")
    elif privateA:print("Class: A, Designation: Private")
    elif privateB:print("Class: B, Designation: Private")
    elif privateC:print("Class: C, Designation: Private")
    elif publicA:print("Class: A, Designation: Public")
    elif publicB:print("Class: B, Designation: Public")
    elif publicC:print("Class: C, Designation: Public")
    elif publicD:print("Class: D, Designation: Public")
    else:print("Class: E, Designation: Public")
    
    print("do you want to try again [Y/N]: ".capitalize())
    x = input()
    if x == "y" or x == "Y":
        solution()
    else:
        exit()
    
if __name__ == '__main__':
    solution()
