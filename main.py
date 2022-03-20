def Class_A(args):
    if 1 <= args[0] <= 127 and args[1] == 0 and args[2] == 0 and args[3] == 0:
        print("class A , designation: public")
    elif args[0] == 10 and 0 <= args[1] <= 255 and 0 <= args[2] <= 255 and 0 <= args[3] <= 255:
        print("class A , designation: Private")
    else:
        print("class A , designation: Special")
def Class_B(args):
    if 128 <= args[0] <= 191 and 0 <= args[1] <= 255 and args[2] == 0 and args[3] == 0:
        print("class B , designation: public")
    elif args[0] == 172 and 16 <= args[1] <= 31 and 0 <= args[2] <= 255 and 0 <= args[3] <= 255:
        print("class B , designation: Private")
    else:
        print("class B , designation: Special")
def Class_C(args):
    if 192 <= args[0] <= 223 and 0 <= args[1] <= 255 and 0 <= args[2] <= 255 and args[3] == 0:
        print("class C , designation: public")
    elif args[0] == 192 and args[1] == 168 and 0 <= args[2] <= 255 and 0 <= args[3] <= 255:
        print("class C , designation: Private")
    else:
        print("class C , designation: Special")
def Class_D(args):
    if 224 <= args[0] <= 239 and 0 <= args[1] <= 255 and 0 <= args[2] <= 255 and 0 <= args[3] <= 255:
        print("class D , designation: public")
    else:
        print("class D , designation: Special")
def Class_E(args):
    if 240 <= args[0] <= 255 and 0 <= args[1] <= 255 and 0 <= args[2] <= 255 and 0 <= args[3] <= 255:
        print("class E , designation: public")
def solution():
    x = input('Enter your IP Address and / Subnet Mask: ')
    a=x.rsplit('.')
    s = a[3].rsplit('/')
    ip=(int(a[0]), int(a[1]), int(a[2]), int(s[0]), int(s[1]))
    if 1 <= ip[0] <= 127:
        Class_A(ip)
    elif 128 <= ip[0] <= 191:
        Class_B(ip)
    elif 192 <= ip[0] <= 223:
        Class_C(ip)
    elif 224 <= ip[0] <= 239:
        Class_D(ip)
    elif 240 <= ip[0] <= 255:
        Class_E(ip)

if __name__ == '__main__':
    solution()
