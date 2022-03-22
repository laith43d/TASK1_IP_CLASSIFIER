import ip

def solution():
    givenIP = input('\nPlease give an IP address (IP/MASK): ')
    try:
        myWorkingIP=ip.checkIP(givenIP)
        print('Class : ' + ip.getClass(myWorkingIP) +', Designation : ' + ip.getDesignation(myWorkingIP))
    except (IndexError, ValueError):
        print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format,' '\n'
        '\tfor example: 192.168.1.1/24, or 10.10.10.1')
        solution()



if __name__ == '__main__':
    solution()















