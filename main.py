
    
def solution(ip):
    ip=ip.split('/')
    p1,p2,p3,p4=map(int, ip[0].split('.'))
    if p1 <=127 and p1>=0 :
        ruselt=("Class: A, Designation: Public")
        if p1==127 and p2==0 :
            ruselt=("Class: A, Designation: Special")
        else:
            ruselt=("Class: A, Designation: Public")
    elif p1==10:
        ruselt=("Class: A, Designation: Private")
    elif p1 <=191 and p1 >=128 :
        ruselt=("Class: B, Designation: Public")
        if p1==172 and p2<=31 and p2>=16:
            ruselt=("Class: B, Designation: Private")
    elif p1 <=223 and p1>=192 :
        ruselt=("Class: C, Designation: Private")
    elif p1==192 and p2==168:
        ruselt=("Class: C, Designation: Public")
    elif p1 <=239 and p1>=224 :
        ruselt=("Class: D, Designation: Public")
    elif p1 <=255 and p1>=240:
        ruselt=("Class: E, Designation: Public")
 
    print(ruselt)

if __name__ == '__main__':
    solution('127.0.0.1/24')
    solution('192.168.1.1/24')
    
    pass
