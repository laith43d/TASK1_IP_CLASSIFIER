def solution(ip):

    # we take the input as a string so we convert it as intergers

    IPslice = ip.split("/")
    net_mask = IPslice[1]
    ipd = IPslice[0].split(".")
    part1 = (int(ipd[0]))
    part2 = (int(ipd[1]))
    part3 = (int(ipd[2]))
    part4 = (int(ipd[3]))
    part5 = (int(net_mask))

# validate the ip adress and subnetmask

    if (part1 < 1 or part1 > 255):
        print('Unvalid IP Adress')

    elif (part2 < 0 or part2 > 255):
        print('Unvalid IP Adress')

    elif (part3 < 0 or part3 > 255):
        print('Unvalid IP Adress')

    elif (part4 < 0 or part4 > 255):
        print('Unvalid IP Adress')

    elif (part5 != 8 and part5 != 16 and part5 != 24):
        print('Unvalid Subnetmask')

    else:
        print("Valid IP adress")

# finding the class by looking at the first octo

    if (part1 > 0 and part1 < 128):
        print('Class: A')
    elif (part1 > 127 and part1 < 192):
        print('Class: B')
    elif (part1 > 191 and part1 < 224):
        print('Class: C')
    elif (part1 > 223 and part1 < 240):
        print('Class: D')
    elif (part1 > 239 and part1 < 256):
        print('Class: E')

# finding out designation

    if (part1 == 10 or part1 == 172 and part2 > 15 and part2 < 30 or part1 == 192 and part2 == 168):
        print('Designation is: Private')
    elif (part1 == 127 and part4 > 0):
        print('Designation is: Special')
    else:
        print('Designation is: Public')


if __name__ == '__main__':

    ip = input("Enter your ip adreess..... \n")
    print("Your IP adress is....  ",ip)

    solution(ip)
