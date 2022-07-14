def solution(ip):
    ip=ip.split("/"); first, second, third, fourth = map(int, ip[0].split('.'))

    if first > 255 or second > 255 or third > 255 or fourth > 255:
        print("INVALID IP ADDRESS")
        exit()

    if 0 < first <= 127:
        classtype = 'A'
        designation = "Public"
        if first == 10:
            designation = 'Private'

        if first == 127:
            designation = "Special"

    if 128 <= first <= 191:
        classtype = 'B'
        designation = "Public"
        if first == 172 and 16 <= second <= 31:
            designation = 'Private'

    if 192 <= first <= 223:
        classtype = 'C'
        designation = "Public"
        if first == 192 and second == 168:
            designation = 'Private'

    if 224 <= first <= 239:
        classtype = 'D'
        designation = "Special"

    if 240 <= first <= 255:
        classtype = 'E'
        designation = "Special"
        
    print("Class: {}, Designation: {}".format(classtype, designation))

if __name__ == '__main__':
    solution(input("Enter IP ADDRESS: "))