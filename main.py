def solution():
    full_ip = input('enter the full ip in the form x.x.x.x/x: ')
    ip = full_ip.split('/')[0]
    subnet = full_ip.split('/')[1]

    octets = ip.split('.')
    first_octet = int(octets[0])
    second_octet = int(octets[1])
    third_octet = int(octets[2])
    fourth_octet = int(octets[3])

    if (first_octet == 10 and 0 <= second_octet <= 255 and 0 <= third_octet <= 255 and 0 <= fourth_octet <= 255) or (first_octet == 169 and second_octet == 254 and 0 <= third_octet <= 255 and 0 <= fourth_octet <= 255) or (first_octet == 172 and 16 <= second_octet <= 31 and 0 <= third_octet <= 255 and 0 <= fourth_octet <= 255) or (first_octet == 192 and second_octet == 168 and 0 <= third_octet <= 255 and 0 <= fourth_octet <= 255):
        print('Private Network')
    elif first_octet == 127 and 0 <= second_octet <= 255 and 0 <= third_octet <= 255 and 1 <= fourth_octet <= 255:
        print('Special Network')
    else:
        print('Public Network')


if __name__ == '__main__':
    solution()
