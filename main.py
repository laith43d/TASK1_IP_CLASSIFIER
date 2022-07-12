def solution(ip):
    print("your IP Address : "+ip)
    ip = ip.split("/")
    ip_split = ip[0].split('.')
    first_part = int(ip_split[0])
    second_part = int(ip_split[1])

    if first_part in range(0, 128):
        print("Class :A ")
        if first_part == 10 and second_part in range(0, 256):
            print("Designation: private")
        elif first_part == 127:
            print("Designation :Special")
        else:
            print("Designation: Public")

    if first_part in range(128, 192):
        print("Class :B ")
        if first_part == 172 and second_part in range(16, 32):
            print("Designation: private")
        else:
            print("Designation: public")

    if first_part in range(192, 224) :
        print("Class :C ")
        if first_part == 192 and second_part == 168 and second_part in range(0, 256):
            print("Designation: private")
        else:
            print("Designation: public")

    if first_part in range(224, 240):
        print("Class :D , Designation: SPECIAL")

    if first_part in range(240, 256):
        print("Class :E , Designation: SPECIAL")


if __name__ == '__main__':
    solution("127.0.0.1/24")
    solution("192.168.1.1/24")
