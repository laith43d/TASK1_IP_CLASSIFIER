def solution(ip):
    ip_with_subnet = ip.split('/')
    ip_split = ip_with_subnet[0].split('.')

    # clase A
    isClassA = int(ip_split[0]) in range(0,128)
    isPrivateClassA = int(ip_split[0]) == 10

    # clase B
    isClassB = int(ip_split[0]) in range(128 ,192)
    isPrivateClassB = int(ip_split[0]) == 172 and  int(ip_split[1]) in range(16 ,32)

    # clase C
    isClassC = int(ip_split[0]) in range(192,224)
    isPrivateClassC = int(ip_split[0]) == 192 and int(ip_split[1]) == 168

    # clase D
    isClassD = int(ip_split[0]) in range(224 ,240)

    # clase E
    isClassE = int(ip_split[0]) in range(240 ,256)


    print ( 'IP is ',ip)

    if  isClassA:
        if isPrivateClassA:
             print("Class A  Private IP")
        else :
             print("Class A  Pubic IP")
    else:
        if isClassB:
            if isPrivateClassB :
                print("Class B  Private IP")
            else:
                print("Class B  Pubic IP")
        else:
            if isClassC:
                if isPrivateClassC :
                    print("Class C  Private IP")
                else:
                    print("Class C  Pubic IP")
            else:
                if isClassD :
                    print(" is Class D ")
                else:
                    if isClassE:
                        print(" is Class E ")
    pass


if __name__ == '__main__':
  ip= "128.0.0.0"

  solution(ip)
  pass