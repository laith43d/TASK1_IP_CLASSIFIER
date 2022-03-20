def solution():
    try:
        def to_list(ip):
            ip2 = []
            temp = ''
            for i in range(0, len(ip)):
                if (ip[i] != '.'):
                    temp += ip[i]
                else:
                    ip2.append(temp)
                    temp = ''
            ip2.append(temp)
            ip2 = [int(x) for x in ip2]
            return ip2

        def a2s(a):
            x = ''
            for i in range(0, len(a)):
                x = x + str(a[i]) + '.'
                return x

        def chk_class(x):
            if (x in range(0, 128)):
                return 'A'
            elif (x in range(128, 192)):
                return 'B'
            elif (x in range(192, 224)):
                return 'C'
            elif (x in range(224, 240)):
                return 'D'
            else:
                return 'E'

        def find_addr(ipclass, ipl):
            if (ipclass == 'A'):
                net_id = a2s(ipl[:1])
                host_id = a2s(ipl[1:])
                start_add = str(net_id) + '0.0.0'
                end_add = str(net_id) + '255.255.255'

            elif (ipclass == 'B'):
                net_id = a2s(ipl[0:2])
                host_id = a2s(ipl[2:])
                start_add = str(net_id) + '0.0'
                end_add = str(net_id) + '255.255'

            elif (ipclass == 'C'):
                net_id = a2s(ipl[0:3])
                host_id = a2s(ipl[3:])
                start_add = str(net_id) + '0'
                end_add = str(net_id) + '255'

            elif(ipclass == 'D'):
                net_id = a2s(ipl[0:4])
                host_id = a2s(ipl[4:])
                start_add = str(net_id)
                end_add = str(net_id)

            elif(ipclass == 'E'):
                net_id = a2s(ipl[0:5])
                host_id = a2s(ipl[5:])
                start_add = str(net_id)
                end_add = str(net_id)

            print("NetID = ", net_id)
            print("HostID = ", host_id)
            print("StartAddress = ", start_add)
            print("EndAddress = ", end_add)

        ip = input("Enter The IP: ")
        ipl = to_list(ip)
        ipclass = chk_class(ipl[0])
        find_addr(ipclass, ipl)
        print("Class = ", ipclass)

        if (ipclass == 'A'):
            if (ipl[0] == 10):
                if (ipl[1] < 255):
                    print('Designation: Private')
                else:
                    print('Designation: Public')

        if (ipclass == 'B'):
            if (ipl[0] == 172):
                if (ipl[1] < 32):
                    print('Designation: Private')
                else:
                    print('Designation: Public')

        if (ipclass == 'C'):
            if (ipl[0] == 192):
                if (ipl[1] == 168):
                    print('Designation: Private')
                else:
                    print('Designation: Public')

        if (ipclass == 'D'):
            print('Designation: Multicast')

        if (ipclass == 'E'):
            print('Designation: Search')
    except:
        print('Error: Invalid IP address')


if __name__ == '__main__':
    solution()
