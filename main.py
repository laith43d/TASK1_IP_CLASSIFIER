def solution(ip):
    newip = ip.split('/')
    newip.pop()
    new = ''
    for i in newip:
        if i != '.':
            new+=i
        sk = new.split('.')
    
    A = sk[0]
    B = sk[1]
    C = sk[2]
    D = sk[3]
    print(" YOUR IP ADDRESS IS ->", ip)
    #CLASS A
    if int(A) == 10 and int(B) in range(0,256) and int(C) in range(0,256) and int(D) in range(0,256):
        print(" CLASS A, Designation: PRIVATE")
    elif int(A) in range(1,128) and int(B) in range(0,1) and int(C) in range(0,1) and int(D) in range(0,1):
        print(" CLASS A,  Designation: PUBLIC")
    elif int(A) == 127 and int(B) in range(0,256) and int(C) in range(0,256) and int(D) in range(0,256):
        print(" CLASS A, Designation: SPECIAL")
    #CLASS B
    if int(A) == 172 and int(B) in range(16,32) and int(C) in range(0,256) and int(D) in range(0,256):
        print(" CLASS B, Designation: PRIVATE")
    elif int(A) in range(128,192) and int(B) in range(0,256) and int(C) in range(0,1) and int(D) in range(0,1):
        print(" CLASS B, Designation: PUBLIC")
    #CLASS C
    if int(A) == 192 and int(B) in range(168,169) and int(C) in range(0,256) and int(D) in range(0,256):
        print(" CLASS C, Designation: PRIVATE")
    elif int(A) in range(192,224) and int(B) in range(0,256) and int(C) in range(0,256) and int(D) in range(0,1):
        print(" CLASS C, Designation: PUBLIC")
    #CLASS D
    if int(A) in range(224,240) and int(B) in range(0,256) and int(C) in range(0,256) and int(D) in range(0,256):
        print(" CLASS D, Designation: SPECIAL")
    #CLASS E
    if int(A) in range(240,256) and int(B) in range(0,256) and int(C) in range(0,256) and int(D) in range(0,256):
        print(" CLASS E, Designation: SPECIAL")
solution('192.168.1.1/24')


if __name__ == '__main__':
    pass
