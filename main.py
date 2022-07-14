import sys
def solution(ip):
    ip_splited = ip.split('/')
    ip_octets = ip_splited[0].split('.')
    ip_octets = [int(i) for i in ip_octets]
    octet1 = ip_octets[0]
    octet2 = ip_octets[1]
    if octet1 == 10:
        print("Class A, Designation: Private")
    elif 127 > octet1 >= 1:
        print("Class A, Designation: Public")
    elif octet1 == 127:
        print("Class A, Designation: Special")
    
    elif octet1 == 172 and 31 >= octet2 >= 16:
        print("Class B, Designation: Private ")
    elif 191 >= octet1 >= 128:
        print("Class B, Designation: Public")
    
    elif octet1 == 192 and octet2 == 168:
        print("Class C, Designation: Private ")
    elif 223 >= octet1 >= 192:
        print("Class C, Designation: Public")
    
    elif 239 >= octet1 >= 224:
        print("Class D, Designation: special")
    
    elif  255 >= octet1 >= 240:
        print("Class D, Designation: special")
    pass

if __name__ == '__main__':
    
    solution(sys.argv[1])
    pass 
