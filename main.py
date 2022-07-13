def solution():
    pass
def solution(ip):
    ip_split=ip.split('/')
    p1,p2,p3,p4=map(int, ip[0].split('.'))
    if p1 <=127 and p1>=0 :
        res=("Class: A, Designation: Public")
        if p1==127 and p2==0 :
            res=("Class: A, Designation: Public")
        else:
            res=("Class: A, Designation: Special")
    elif p1==10:
        res=("Class: A, Designation: Private")
    elif p1 <=191 and p1 >=128 :
        res=("Class: B, Designation: Public")
        if p1==172 and p2<=31 and p2>=16:
            res=("Class: B, Designation: Private")
    elif p1 <=223 and p1>=192 :
        res=("Class: C, Designation: Public")
    elif p1==192 and p2==168:
        res=("Class: C, Designation: Private")
    elif p1 <=239 and p1>=224 :
        res=("Class: D, Designation: Public")
    elif p1 <=255 and p1>=240:
        res=("Class: E, Designation: Public")
   # elif (p1 >255)or (p2 >255)  or (p1 <0)or(p2 <0) :
      #  res="The ip out of the range"
    print(res)

if __name__ == '__main__':
    pass
    ip='192.168.1.1/24'
    
    solution(ip)
