def solution(ip):
    
    ip_split=ip.split('.')
    out1="Class: "
    out2="Designation: "
    fp=int(ip_split[0])
    if fp>=1 and fp<=127:
        print(out1+"A")
        if fp==10:
            print(out2+"private")
        else:
            print(out2+"public")
    elif fp>=128 and fp<=191:
        print(out1+"B")
        if fp==172:
            print(out2+"private")
        else:
            print(out2+"public")
    elif fp>=192 and fp<=223:
        print(out1+"C")
        if fp==192:
            print(out2+"private")
        else:
            print(out2+"public")
    elif fp>=224 and fp<=239:
        print(out1+"D")
    elif fp>=240 and fp<=255:
        print(out1+"E")

if __name__ == '__main__':
    ip = input("Enter Your Ip Address: ")
    solution(ip)
