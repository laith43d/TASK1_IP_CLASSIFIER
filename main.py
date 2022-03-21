import ip

def solution():
    pass

givenIP = input('\nPlease give an IP address (IP/MASK): ')
try:
    myWorkingIP=ip.checkIP(givenIP)
    print('Your IP     : ' + myWorkingIP[1])
    print('Class       : ' + ip.getClass(myWorkingIP[0]))
    print('Designation : ' + ip.getDesignation(myWorkingIP[0]))
except (IndexError, ValueError):
    print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format,' '\n'
    '\tfor example: 192.168.1.1/24, or 10.10.10.1/28')
    main()

if __name__ == '__main__':
    solution()
    pass














