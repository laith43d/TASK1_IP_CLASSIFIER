def solution():

    ipa = input('\nPlease write an IP address: ')

    # split the ip mask from input
    mask = ipa.split('/')

    # split ip Octets
    split_ip = mask[0]
    int_ip = split_ip.split('.')

    # converting all string elements in int_ip list to integers
    for i in range(0, len(int_ip)):
        int_ip[i] = int(int_ip[i])

    # determining the class and desgtnation of the ip
    ipclass = ''
    desgnation = ''
    if 127 >= int_ip[0] >=1:
        ipclass = 'A'
        if int_ip[0] == 10 and 255 >= int_ip[1] >= 0:
            desgnation = 'Private'
        else:
            desgnation = 'Public'

    elif 191 >= int_ip[0] >=128:
        ipclass = 'B'
        if int_ip[0] == 172 and 31 >= int_ip[1] >= 16:
            desgnation = 'Private'
        else:
            desgnation = 'Public'

    elif 223 >= int_ip[0] >=192:
        ipclass = 'C'
        if int_ip[0] == 192 and int_ip[1] == 168:
            desgnation = 'Private'
        else:
            desgnation = 'Public'

    elif 239 >= int_ip[0] >=224:
        ipclass = 'D'
        desgnation = 'Special'
    elif 255 >= int_ip[0] >=240:
        ipclass = 'E'
        desgnation = 'Special'

    if int_ip[0] == 127 and 255 >= int_ip[3] >= 1:
        ipclass='C'
        desgnation = 'Special'

    print('\nClass: {}, Desgnation: {} \n'.format(ipclass,desgnation))


if __name__ == '__main__':
    solution()
