def solution():
    ipa = input('\nPlease give an IP address: ')
    mask = ipa.split('/')
    split_ip = mask[0]
    int_ip = split_ip.split('.')

    for i in range(0, len(int_ip)):
        int_ip[i] = int(int_ip[i])








if __name__ == '__main__':
    solution()
