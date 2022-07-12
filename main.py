def solution(ip):
    ip_mask = ip.split('/')
    ip_class = ip_mask[0].split('.')
    while True:
        try:
            if 0 <= int(ip_class[0]) <= 127:
                if int(ip_class[0]) == 127:
                    return 'class: A, designation: special'
                elif int(ip_class[0]) == 10:
                    return 'class: A, designation: private'
                elif 0 <= int(ip_class[0]) <= 9 or 11 <= int(ip_class[0]) <= 126:       # delete
                    return 'class: A, designation: public'

            elif 128 <= int(ip_class[0]) <= 191:
                if int(ip_class[0]) == 172 and 16 <= int(ip_class[1]) <= 31:
                    return 'class: B, designation: private'
                else:
                    return 'class: B, designation: public'

            elif 192 <= int(ip_class[0]) <= 223:
                if int(ip_class[0]) == 192 and int(ip_class[1]) == 168:
                    return 'class: C, designation: private'
                else:
                    return 'class: C, designation: public'

            elif 224 <= int(ip_class[0]) <= 239:
                return 'class D'

            elif 240 <= int(ip_class[0]) <= 255:
                return 'class  E'

        except ValueError as e:
            ip_class = input('your ip address is invalid try again:')


if __name__ == '__main__':
    print(solution('127.0.0.1/24'))
    print(solution('192.168.1.1/24'))
