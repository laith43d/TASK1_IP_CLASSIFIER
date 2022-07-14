
def solution():
    ip = input('Enter ip address (x.x.x.x) : ')
    ip_dot = ip.split('.')

    if ip_dot[0] == '10':
        print('class: A, Designation: Privte')
   
    elif ip_dot[0] == '172' and 16 <= int(ip_dot[1]) <= 31:
        print('Class : B, , Designation: Private')
    
    elif ip_dot[0] == '192' and ip_dot[1] == '168':
        print('Class : C, Designation: Private' )

    elif 1 <= int(ip_dot[0]) <= 126:
        print('Class : A, Designation: Public')

    elif ip_dot[0] == '127':
        print('Class : A, Designation: Special')

    elif 128 <= int(ip_dot[0]) <= 191:
        print('Class : B, Designation: Public')

    elif 192 <= int(ip_dot[0]) <= 223:
        print('Class : C, Designation: Public')

    elif 224 <= int(ip_dot[0]) <= 239:
        print('Class : D, Designation: Special')

    elif 240 <= int(ip_dot[0]) <= 255:
        print('Class : E, Designation: Special')

    else:
        print('incorrect ip address')

if __name__ == '__main__':
    try:
       solution()
    except ValueError:
        print('enter valid ip address')
        solution()
                            