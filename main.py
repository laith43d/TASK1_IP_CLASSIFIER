def solution(ip_address):
    ip_address = ip_address.split(".")

    if 0 < int(ip_address[0]) <= 127:
        if int(ip_address[0]) == 10 and (0 <= int(ip_address[1]) <= 255) and\
                (0 <= int(ip_address[1]) <= 255) and (0 <= int(ip_address[3].split("/")[0]) <= 255):
            print("Class: A, Designation: Private")
        elif int(ip_address[1]) == 0 and int(ip_address[2]) == 0 and int(ip_address[3].split("/")[0]) == 0:
            print("Class: A, Designation: Public")
        elif int(ip_address[0]) == 127 and (0 <= int(ip_address[1]) <= 255) and\
                (0 <= int(ip_address[1]) <= 255) and (1 <= int(ip_address[3].split("/")[0]) <= 255):
            print("Class: A, Designation: Special")

    elif 128 <= int(ip_address[0]) <= 191:
        if int(ip_address[0]) == 172 and (16 <= int(ip_address[1]) <= 31):
            print("Class: B, Designation: Private")
        elif (0 <= int(ip_address[1]) <= 255) and (int(ip_address[2]) == 0) and\
                (int(ip_address[3].split("/")[0]) == 0):
            print("Class: B, Designation: Public")

    elif 192 <= int(ip_address[0]) <= 223:
        if int(ip_address[0]) == 192 and int(ip_address[1]) == 168:
            print("Class: C, Designation: Private")
        elif (0 <= int(ip_address[1]) <= 255) and (0 <= int(ip_address[2]) <= 255) and\
                (int(ip_address[3].split("/")[0]) == 0):
            print("Class: C, Designation: Public")

    elif 224 <= int(ip_address[0]) <= 239:
        print("Class: D")

    elif 240 <= int(ip_address[0]) <= 255:
        print("Class: E")


if __name__ == '__main__':
    user_ip = input("Enter your IP Address: ")
    solution(user_ip)
