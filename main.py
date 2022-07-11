def solution():
    pass

    ip = str(input('Enter IP address: '))
    divideIp = ip.split('/')[0].split('.')
    if ((len(divideIp) != 4) and (divideIp[0] not in range(0,255) )and
         (divideIp[1] not in range(0,255)) and 
         (divideIp[2] not in range(0,255)) and
          (divideIp[3] not in range(0,255))):
         print('IP address error .xxx.xxx.xxx.xxx represents the IP address ')
    
    else:
        firstDivideIp, secondDivideIp, thirdDivideIp,fourthDivideIp = int(divideIp[0]), int(divideIp[1]),int(divideIp[2]), int(divideIp[3])
    
        if  firstDivideIp in range(0  , 128) :
            if firstDivideIp ==0: 
                print('class: Class A, designation: Private')
            elif firstDivideIp == 127 and fourthDivideIp != 0:
                print('class: Class A, designation: Special')
            else: print('class: Class A, designation: Public')
        elif firstDivideIp in range(128, 192):
            if  firstDivideIp ==172 and secondDivideIp in range(16,32): 
                print('class: Class B, designation: Private')
            else:print('class: Class B, designation: Public')
        elif firstDivideIp in range(192, 224):
            if  firstDivideIp ==192 and secondDivideIp ==168: 
                print('class: Class C, designation: Private')
            else:print('class: Class C, designation: Public')
        
        elif firstDivideIp in range(224, 240):
            print('class: Class D, designation: Special')
        else:
            print('class: Class E, designation: Special')

   


if __name__ == '__main__':
    pass
    solution()
