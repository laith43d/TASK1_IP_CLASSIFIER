def solution():
    pass


def solution(ip):
    ip1=ip.split("/")
    ip_parts=ip1[0].split(".")
    part1=(int(ip_parts[0]))
    part2=(int(ip_parts[1]))
    part4=(int(ip_parts[3]))
    
    if (0 < part1 < 127):
        print("Class: A, Designation: Public")
    elif (part1 == 10):
        print("Class: A, Designation: Private")
    elif (part1 == 127) and (1 <= part4 <= 255):
        print("Class: A, Designation: Special")
        
    elif (128 >= part1 >= 191):
        print("Class: B, Designation: Public")
    elif (part1 == 172) and (16 <= part2 <= 13):
        print("Class: B, Designation: Private")
        
    elif (192 >= part1 >= 223):
        print("Class: C, Designation: Public")
    elif (part1 == 192) and ( part2 == 168):
        print("Class: C, Designation: Private")
    
    elif (224 >= part1 >= 239):
        print("Class: D, Designation: Public")
        
    elif (240 >= part1 >= 255):
        print("Class: E, Designation: Public")   
ip = input("inter the IP:")
solution(ip)   
    
if __name__ == '__main__':
    pass

