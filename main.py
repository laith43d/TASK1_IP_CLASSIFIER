def solution():
    ip = input(str("input the IP address "))
    print("the IP: "+ip)
    ip = ip.split("/")
    ip_split = ip[0].split('.')
    first_part = ip_split[0]
    second_part = ip_split[1]

    if str(0) <= first_part < str(128):
        print("Class :A ")
        if first_part == str(10) and str(0) <= second_part < str(256):
            print("Designation: private")
        elif first_part == str(127):
            print("Designation :Special")
        else:
            print("Designation: Public")

    if str(128) <= first_part < str(192):
        print("Class :B ")
        if first_part == str(172) and str(16) <= second_part < str(32):
            print("Designation: private")
        else:
            print("Designation: public")

    if str(192) <= first_part < str(224) :
        print("Class :C ")
        if first_part == str(192) and second_part == str(168) and str(16) <= second_part < str(32):
            print("Designation: private")
        elif first_part == str(127):
            print("Designation: special")
        else:
            print("Designation: public")

    if str(224) <= first_part < str(240):
        print("Class :D ")

    if str(240) <= first_part < str(256):
        print("Class :E ")


if __name__ == '__main__':
    solution()
