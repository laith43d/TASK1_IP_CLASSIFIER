def ipSolution():
    # input ip-address
    ip = input('Enter your Ip-address and mask  IP/Mask: ')
    ip = ip.split('/')
    mask = ip[1]
    ipAddress = ip[0].split('.')

    # Ip check
    i = 0
    while i < len(ipAddress):
        if 0 <= int(ipAddress[i]) <= 255:
            isRange = True
        else:
            isRange = False
        i += 1

    # type of class
    if 0 <= int(ipAddress[0]) <= 127:
        typeClass = 'A'
    elif 128 <= int(ipAddress[0]) <= 191:
        typeClass = 'B'
    elif 192 <= int(ipAddress[0]) <= 223:
        typeClass = 'C'
    elif 224 <= int(ipAddress[0]) <= 239:
        typeClass = 'D'
    elif 240 <= int(ipAddress[0]) <= 255:
        typeClass = 'E'

    # designation
    if int(ipAddress[0]) == 127 and 0 <= int(ipAddress[1]) <= 255 and 0 <= int(ipAddress[2]) <= 255 and 1 <= int(
            ipAddress[3]) <= 255:
        desingation = 'Special'
    elif typeClass == 'A':
        if int(ipAddress[0]) == 10 and 0 <= int(ipAddress[1]) <= 255 and 0 <= int(ipAddress[2]) <= 255 and 0 <= int(
                ipAddress[3]) <= 255:
            desingation = 'Private'
        else:
            desingation = 'Public'
    elif typeClass == 'B':
        if int(ipAddress[0]) == 169 and int(ipAddress[1]) == 254 and 0 <= int(ipAddress[2]) <= 255 and 0 <= int(
                ipAddress[3]) <= 255 or int(ipAddress[0]) == 172 and 16 <= int(ipAddress[1]) <= 31 and 0 <= int(
            ipAddress[2]) <= 255 and 0 <= int(
            ipAddress[3]) <= 255:
            desingation = 'Private'
        else:
            desingation = 'Public'
    elif typeClass == 'C':
        if int(ipAddress[0]) == 192 and int(ipAddress[1]) == 168 and 0 <= int(ipAddress[2]) <= 255 and 0 <= int(
                ipAddress[3]) <= 255:
            desingation = 'Private'
        else:
            desingation = 'Public'

    # Print output
    if isRange == True:
        print('Output: Class: ' + typeClass + ',' + ' Designation: ' + desingation)
    else:
        print('Invalid Ip-Address')


if __name__ == '__main__':
    ipSolution()
