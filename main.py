import re

def solution():
    while True:
        ip = input('Enter an IP address in the format #.#.#.#/# :\n')
        if is_valid(ip):
            ip_octets = split_ip(ip)
            ip_octets = [int(i) for i in ip_octets]
            ip_class = find_class(ip_octets[0])
            ip_designation = find_designation(ip_octets)
            print(f'Class: {ip_class}, Designation: {ip_designation}')
            break
        else:
            print('Please try again...\n')
            continue


def is_valid(str_ip):
    pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}")
    checker = pattern.match(str_ip)

    if not checker:
        print('The IP address does not match the required format')
        return False

    ip = split_ip(str_ip)

    for i in ip:
        if (int(i) not in range(0, 256)):
            print('All ocetets should be in range 0-255')
            return False

        if len(i) > len(i.lstrip('0')) and len(i) != 1:
            print('Leading zeros in any octet are not allowed')  # 01 or 001
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
    if any ([
        ip_octets[0] == 10 ,
        ip_octets[0] == 169 and ip_octets[1] == 254 ,
        ip_octets[0] == 172 and ip_octets[1] in range(16, 32) ,
        ip_octets[0] == 192 and ip_octets[1] == 168
    ]):
        return 'Private'

    elif (
        ip_octets[0] == 127
    ):
        return 'Special'

    else:
        return 'Public'


if __name__ == '__main__':
    solution()
