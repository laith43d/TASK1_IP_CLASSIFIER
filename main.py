def solution(ip):
    sk = ip.split('.')
    print(" YOUR IP-> ", ip)
    #CLASS A
    if int(sk[0]) == 127 and int(sk[3]) in range(1,256):
        return " CLASS A, Designation: SPECIAL"
    elif int(sk[0]) == 10:
        return " CLASS A, Designation: PRIVATE"
    elif int(sk[0]) in range(1,128):
        return " CLASS A,  Designation: PUBLIC"
    #CLASS B
    if int(sk[0]) == 172:
        return " CLASS B, Designation: PRIVATE"
    elif int(sk[0]) in range(128,192):
        return " CLASS B, Designation: PUBLIC"
    #CLASS C
    if int(sk[0]) == 192 and int(sk[1]) == 168:
        return " CLASS C, Designation: PRIVATE"
    elif int(sk[0]) in range(192,224):
        return " CLASS C, Designation: PUBLIC"
    #CLASS D
    if int(sk[0]) in range(224,240):
        return " CLASS D, Designation: SPECIAL"
    #CLASS E
    if int(sk[0]) in range(240,256):
        return " CLASS E, Designation: SPECIAL"
    
if __name__ == '__main__':
    print(solution('127.0.0.0'))
