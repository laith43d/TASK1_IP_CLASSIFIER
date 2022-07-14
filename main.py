def solution():
    ip = '192.168.1.1/24'
    ip_splited = ip.split('/')
    ip_octets = ip_splited[0].split('.')
    print(ip_octets)
    ip_octets = [int(i) for i in ip_splited]
    pass

if __name__ == '__main__':
    solution()
    pass 
