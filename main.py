from ipaddress import ip_address


def solution(ip_address):
    ip = ip_address.split(".")
    x = int(ip[0])
    y = int(ip[1])
    z = int(ip[2])
    w = int(ip[3])
    if x in range(1, 128) and (0 <= int(y) <= 255) and \
            (0 <= int(z) <= 255) and \
            (1 <= int(w) <= 255):
        print("class A, Special")
    elif x == 10 and (0 <= int(y) <= 255):
        print('Class A, Private')
    elif x in range(1, 128):
        print('Class A, Public')

    elif x == 169 and y == 254 and \
            (0 <= int(z) <= 255) and (0 <= int(w) <= 255):
        print("Class B, APIPA")
    elif x == 172 and (31 >= int(y) >= 16):
        print('Class B, Private')
    elif 128 <= int(x) <= 191:
        print('Class B, Public')

    elif x == 192 and y == 168:
        print('Class C, Private')
    elif 192 <= int(x) <= 223:
        print('Class C, Public')

    elif 224 <= int(x) <= 239:
        print('Class D')

    elif 240 <= int(x) <= 255:
        print('Class E')

    else:
        print("IP Address incorrect")



if __name__ == '__main__':
    input = "10.255.0.0"
    solution(input)
