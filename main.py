def solution():

    ipa = input('\nPlease give an IP address: ')

    # split the ip mask from input
    mask = ipa.split('/')

    # split ip Octets
    split_ip = mask[0]
    int_ip = split_ip.split('.')

    # converting all string elements in int_ip list to integers
    for i in range(0, len(int_ip)):
        int_ip[i] = int(int_ip[i])

    # determining the class of the ip
    ipclass = ''
    if 127 >= int_ip[0] >=1:
        ipclass = 'Class A'
    elif 191 >= int_ip[0] >=128:
        ipclass = 'Class B'
    elif 223 >= int_ip[0] >=192:
        ipclass = 'Class C'
    elif 239 >= int_ip[0] >=224:
        ipclass = 'Class D'
    elif 255 >= int_ip[0] >=240:
        ipclass = 'Class E'








if __name__ == '__main__':
    solution()
