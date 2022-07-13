def solution():
    pass

ip='172.16.1.1/24'
sub_ip = ip.split('/')
f_ip = sub_ip[0].split('.')
f_ip = [int(i) for i in f_ip]
if 0 <= f_ip[0] <= 9:
    print('Class: A, Designation: Public')
elif f_ip[0] == 10:
    print('Class: A, Designation: Private')    
elif 11 <= f_ip[0] <= 126:
    print('Class: A, Designation: Public')
elif f_ip[0] == 127:
    print('Class: A, Designation: Special')
elif 128 <= f_ip[0] <= 172 and f_ip[1] not in range(16,31) :
    print('Class: B, Designation: Public')
elif f_ip[0] == 172 and 16 <= f_ip[1] <= 31:
    print('Class: B, Designation: Private')
elif 173 <= f_ip[0] <= 191:
    print('Class: B, Designation: Public')
elif f_ip[0] == 192 and f_ip[1] != 168:
    print('Class: C, Designation: Public')
elif f_ip[0] == 192 and f_ip[1] == 168:
    print('Class: C, Designation: Private')
elif 193 <= f_ip[0] <= 223:
    print('Class: C, Designation: Public')
elif 224 <= f_ip[0] <= 239:
    print('Class: D, Designation: Special')
elif 240 <= f_ip[0] <= 255:
    print('Class: E, Designation: Special')

if __name__ == '__main__':
    pass
