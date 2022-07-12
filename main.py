def solution():
    while True:
        ip = input('Enter an IP address in the format x.x.x.x/x :\n')
        if is_valid(ip):
            ip_octets = split_ip(ip)
            ip_octets = [int(i) for i in ip_octets]
            ip_class = find_class(ip_octets[0])
            ip_designation = find_designation(ip_octets)
            print(f'Class: {ip_class}, Designation: {ip_designation}')
            break

        else:
            print('Please try again...')
            continue


def is_valid(str_ip):
    ip = split_ip(str_ip)

    if len(ip) != 4:
        print('The number of octets should equel four')
        return False

    for i in ip:
        if (not i.isdigit()):
            print('All octets should be numeric')
            return False
        elif (i.isdigit() and int(i) not in range(0, 256)):
            print('All ocetets should be in range 0-255')
            return False

    cidr_index = str_ip.find('/')+1
    if int(str_ip[cidr_index:]) not in range(0, 33):
        print('CIDR notation should be between 0-32')
        return False

    return True


def split_ip(str_ip):
    ip_octets = str_ip.split('/')[0].split('.')
    return ip_octets


def find_class(first_octete):
    if first_octete in range(1, 128):
        return 'A'
    if first_octete in range(128, 192):
        return 'B'
    if first_octete in range(192, 224):
        return 'C'
    if first_octete in range(224, 240):
        return 'D'
    if first_octete in range(240, 256):
        return 'E'


def find_designation(ip_octets):
    ''''
    Private IP :
        10.0.0.0 — 10.255.255.255
        169.254.0.0 - 169.254.255.255
        172.16.0.0 - 172.31.255.255 
        192.168.0.0 - 192.168.255.255
    Special IP :
        127.0.0.1 - 127.255.255.255
    Any range else :
        Public IP 
    '''
    if any ([
        ip_octets[0] == 10 ,
        ip_octets[0] == 169 and ip_octets[1] == 254 ,
        ip_octets[0] == 172 and ip_octets[1] in range(16, 32) ,
        ip_octets[0] == 192 and ip_octets[1] == 168
    ]):
        return 'Private'

    elif all ([
        ip_octets[0] == 127 ,
        ip_octets[-1] in range(1, 256)
    ]):
        return 'Special'

    else:
        return 'Public'


if __name__ == '__main__':
    solution()
