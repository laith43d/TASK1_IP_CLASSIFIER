ip = '192.168.0.1'
parts = ip.split('.')
print(parts)
ip_0 =parts[0]
ip_1 = parts[1]
ip_2 = parts[2]
ip_3 = parts[3]
sep = ('.')
print(ip_0 + sep +ip_1 + sep +ip_2 + sep + ip_3 )

if parts[0] == '192':
    print('class = C , designation public ip ')
elif parts[0] == '126':
    print('class = B , designation public ip ')
elif parts[0] == '10':
    print('class = A , designation public ip ')
elif parts[0] == '127' and parts[3] == '1':
    print('it designation as special ip Address ')
else:
    print('enter yuor ip addres correct')
