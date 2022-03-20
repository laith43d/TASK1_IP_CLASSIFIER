def class_a(lip):

    # Public IP Range: 1.0.0.0 to 127.0.0.0
    if (lip[0] in range(0, 128)) and lip[1] == 0 and 0 == lip[2] and 0 == lip[3]:
        print("class A, Designation: public ip")
    elif (lip[0] == 10) and lip[1] <= 255 and lip[2] <= 255 and lip[3] <= 255:
        print("class A, Designation: private ip")


def class_b(lip):

    # Public IP Range: 128.0.0.0 to 191.255.0.0
    if (lip[0] in range(128, 192)) and lip[1] <= 255 and lip[2] == 0 and lip[3] == 0:
        print("class B, Designation: public ")
    elif lip[0] == 172 and (lip[1] in range(16, 32)) and lip[2] <= 255 and lip[3] <= 255:
        print("class B, Designation: private")


def class_c(lip):

    # Public IP Range: 192.0.0.0 to 223.255.255.0
    if (lip[0] in range(192, 223)) and lip[1] <= 255 and lip[2] <= 255 and lip[3] == 0:
        print("class C, Designation: public ")
    elif lip[0] == 192 and lip[1] == 168 and lip[2] <= 255 and lip[3] <= 255:
        print("class C, Designation: private")


def class_d(lip):

    # range: 224.0.0.0 to 239.255.255.255
    if lip[0] in range(224, 240):
        print("class D")


def class_e(lip):

    # range: 240 to 255
    if (lip[0] in range(240, 256)) and lip[1] <= 255 and lip[2] <= 225 and lip[3] <= 225:
        print("class E")


def special(lip):

    if lip[0] == 127 and (lip[3] in range(1, 256)):
        print("class A, special ip")


def solution():
    full_ip_address = input("Enter  the IP address")
    ip = [i for i in full_ip_address.split("/")]
    lip = [int(i) for i in ip[0].split('.')]
    for k in lip:
        if k < 0 or k > 255:
            print("invalid ip ")
            break
    class_a(lip)
    class_b(lip)
    class_c(lip)
    class_d(lip)
    class_e(lip)
    special(lip)


if __name__ == '__main__':
    solution()
