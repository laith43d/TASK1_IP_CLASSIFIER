input_ip = input("Input IP Address: ").split('/')
ip = str(input_ip[0]).split('.')


def is_ip_valid(ip_add):
    """ Take IP Address (as list) to check its validity and return bollen value (True if valid / False if invalid) """
    if len(ip_add) > 4:
        if 0 <= int(ip_add) <= 255:
            return False
        return False
    else:
        return True


def class_checker(ip_address):
    """Take Ip Address (as list) to check its corresponding class (A ,B ,C ,D ,E)"""
    if 0 <= int(ip_address[0]) <= 127:
        return "Class A"
    elif 128 <= int(ip_address[0]) <= 191:
        return "Class B"
    elif 192 <= int(ip_address[0]) <= 223:
        return "Class C"
    elif 224 <= int(ip_address[0]) <= 239:
        return "Class D"
    elif 240 <= int(ip_address[0]) <= 255:
        return "Class E"


def privet_ip_checker(ip_address):
    """Take IP Address (as list) and return 'Privet IP Address' if its privet """
    class_type = class_checker(ip_address)
    if class_type == "Class A" and int(ip_address[0]) == 10 and 0 <= int(ip_address[1]) <= 255:
        if 0 <= int(ip_address[2]) <= 255 and 0 <= int(ip_address[3]) <= 255:
            return "Privet IP Address"
    elif class_type == "Class B" and int(ip_address[0]) == 169 and int(ip_address[1]) == 254:
        if 0 <= int(ip_address[2]) <= 255 and 0 <= int(ip_address[3]) <= 255:
            return "Privet IP Address"
    elif class_type == "Class B" and int(ip_address[0]) == 172 and 16 <= int(ip_address[1]) <= 31:
        if 0 <= int(ip_address[2]) <= 255 and 0 <= int(ip_address[3]) <= 255:
            return "Privet IP Address"
    elif class_type == "Class C" and int(ip_address[0]) == 192 and int(ip_address[1]) == 168:
        if 0 <= int(ip_address[2]) <= 255 and 0 <= int(ip_address[3]) <= 255:
            return "Privet IP Address"


def special_ip_checker(ip_address):
    """Take IP Address (as list) and return 'Special IP Address' if its special """
    class_type = class_checker(ip_address)
    if int(ip_address[0]) == 127 and 0 <= int(ip_address[1]) <= 255:
        if 0 <= int(ip_address[2]) <= 255 and 1 <= int(ip_address[3]) <= 255:
            return "Special IP Address"
    elif class_type == "Class E" or class_type == "Class D":
        return "Special IP Address"


def ip_checker(ip_address):
    """Take IP Address (as list) and Subnet Mask (as int) and return 'Class and type of ip address' """
    special_ip = ''
    privet_ip = ''
    public_ip = ''
    if is_ip_valid(ip_address):
        if special_ip_checker(ip_address) == "Special IP Address":
            special_ip = special_ip_checker(ip_address)
        elif privet_ip_checker(ip_address) == "Privet IP Address":
            privet_ip = privet_ip_checker(ip_address)
        else:
            public_ip = "Public IP"
        class_type = class_checker(ip_address)
        print(f"{class_type}, Designation: {special_ip}{privet_ip}{public_ip}")
    else:
        print("Invalid IP Address")


def solution():
    ip_checker(ip)


if __name__ == '__main__':
    solution()
