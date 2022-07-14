import sys

def solution(ipAddress):
    pass
    
    # variables declaration
    classIP = ''
    designationIP = ''
    
    ip = [0, 0, 0, 0]
    findError = False
    while True:
        try:
            if findError: ipAddress = input('please, Enter a valid IPv4 address in #.#.#.#/# format, (to exit type "x"): \n')
            if ipAddress == 'x' or ipAddress == 'X': sys.exit()
            
            # Split user's input based on '/'
            ipMask = ipAddress.split('/')
            splitIP = ipMask[0]
            
            # convert data type of splitIP form str to int
            ip = [int(i) for i in splitIP.split('.')]
            
            # check every single number is in the range
            if ip[0] not in range(1, 256):
                print('The number you entered:', ip[0], 'is out of range [1-255]')
            elif ip[1] not in range(0, 256):
                print('The number you entered:', ip[1], 'is out of range [0-255]')
            elif ip[2] not in range(0, 256):
                print('The number you entered:', ip[2], 'is out of range [0-255]')
            elif ip[3] not in range(0, 256):
                print('The number you entered:', ip[3], 'is out of range [0-255]')
            
            break
        except ValueError as valueError:
            findError = True
            print('The IP address you entered Contains symbols or characters that are not allowed')
        except IndexError as indexError:
            findError = True
            print('The IP address you entered does not contain the required length')

    # check the ip address to which class it belongs and what his a designation
    if ip[0] >= 1 and ip[0] <= 127:
        classIP = 'A'
        designationIP = 'Public'
        if ip[0] == 127: designationIP = 'Special'
        elif ip[0] == 10: designationIP = 'Private'
    elif ip[0] >= 128 and ip[0] <= 191:
        classIP = 'B'
        designationIP = 'Public'
        if (i[0] == 172 and i[1] >= 16 and i[1] <= 31) or ([0] == 169 and i[1] == 254): designationIP = 'Private'
    elif ip[0] >= 192 and ip[0] <= 223:
        classIP = 'C'
        designationIP = 'Public'
        if ip[0] == 192 and ip[1] == 168: designationIP = 'Private'
    elif ip[0] >= 224 and ip[0] <= 239:
        classIP = 'D'
        designationIP = 'Special'
    else :
        classIP = 'E'
        designationIP = 'Special'
    
    print('Class:', classIP, 'Designation:', designationIP)

if __name__ == '__main__':
    pass
    solution('127.0.0.1/24')