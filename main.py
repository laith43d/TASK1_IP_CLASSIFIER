
def solution(ip_address1):
    ip = ip_address1
    ip_address1 = input("Enter Ip Address:")
    ip_address1=ip_address1.split('.')
    ip_address1 = [int (i) for i in ip_address1]
    if ip_address1.__len__ <4:
        print("ip address is false value! rewrite:")
        solution(ip)
    elif ip_address1[0] <0 or  ip_address1[1] <0 or ip_address1[2] <0 or ip_address1[3] <0 :
        print("ip address is false value! rewrate:")
        solution(ip)

    # ip class type
    if ip_address1[0] in range(0, 128):  
        print("The Class Type Is A")
    elif ip_address1[0] in range(127, 192):
        print("The Class Type Is B")
    elif ip_address1[0] in range(191, 224):
        print("The Class Type Is C")
    elif ip_address1[0] in range(223, 240):
        print("The Class Type Is D")
     

    # Designation
    if ip_address1[0] == 10 or  ip_address1[0]==169 and  ip_address1[1]==254 or  ip_address1[0] == 172 and  ip_address1[1] > 15 and  ip_address1[1] < 30 or  ip_address1[0] == 192 and  ip_address1[1] == 168:
        print("The Designation Is : Private")

    elif ip_address1[0] == 127 and ip_address1[3] > 0:
        print("The Designation Is : Special")

    else:
        print("The Designation Is : Public")
if __name__ == '__main__':
    in_ip="127.0.0.1/24"
solution(in_ip)      
