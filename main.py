def solution(ip):
    ip=ip.split('/')
    num1,num2,num3,num4=map(int, ip[0].split('.'))
    if num1 <=127 and num1>=0 :
        res=("Class: A, Designation: Public")
        if num1==127 and num2==0 and num3==0 and num4==0:
            res=("Class: A, Designation: Public")
        else:
            res=("Class: A, Designation: Special")
    elif num1==10:
        res=("Class: A, Designation: Private")
    elif num1 <=191 and num1 >=128 :
        res=("Class: B, Designation: Public")
        if num1==172 and num2<=31 and num2>=16:
            res=("Class: B, Designation: Private")
    elif num1 <=223 and num1>=192 :
        res=("Class: C, Designation: Public")
    elif num1==192 and num2==168:
        res=("Class: C, Designation: Private")
    elif num1 <=239 and num1>=224 :
        res=("Class: D, Designation: Public")
    elif num1 <=255 and num1>=240:
        res=("Class: E, Designation: Public")
    elif (num1 or num2 or num3 or num4 ) >255 or (num1 or num2 or num3 or num4 ) <0:
        res="The ip out of the range"
    print(res)


    


if __name__ == '__main__':
    ip=input("Enter the ip Address: ")
    solution(ip)
