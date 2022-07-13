def solution():
    import sys
    user_input = input("Enter an ip address, press 'x' to exit: ")
    if user_input == 'x' or user_input == 'X':
        sys.exit()
    ip_with_mask = user_input.split('/')
    ip_split = ip_with_mask[0].split('.')

    ip_first_part = int(ip_split[0])
    ip_second_part = int(ip_split[1])
    ip_threed_part = int(ip_split[2])
    ip_fourth_part = int(ip_split[3])

    if ip_first_part < 1 or ip_first_part > 255:
        print('Invalid IP Address')
        sys.exit()
    elif ip_second_part < 0 or ip_second_part > 255:
        print('Invalid IP Address')
        sys.exit()
    elif ip_threed_part < 0 or ip_threed_part > 255:
        print('Invalid IP Address')
        sys.exit()
    elif ip_fourth_part < 0 or ip_fourth_part > 255:
        print('Invalid IP Address')
        sys.exit()

    if ip_first_part in range(1, 128):
        if ip_first_part == 10:
            print('Class: A, Designation: Private')
        elif ip_first_part == 127:
            print('Class: A, Designation: Special')
        else:
            print('Class: A, Designation: Public')

    elif ip_first_part in range(128, 192):
        if ip_first_part == 172 and ip_second_part in range(16, 32):
            print('Class: B, Designation: Private')
        elif ip_first_part == 169 and ip_second_part == 254:
            print('Class: B, Designation: Private')
        else:
            print('Class: B, Designation: Public')

    elif ip_first_part in range(192, 224):
        if ip_first_part == 192 and ip_second_part == 168:
            print('Class: C, Designation: Private')
        else:
            print('Class: C, Designation: Public')

    elif ip_first_part in range(224, 240):
        print('Class: D,Designation: Special')

    elif ip_first_part in range(240, 256):
        print('Class: E, Designation: Special')

    else:
        print('This IP Address you entered is not valid..\nPlease try again')


if __name__ == '__main__':
    solution()