import sys
# Print the Class and Designation of IP Address
# Classes: A, B, C, D, E
# Designation: Private, Public, Special
# Run: python main.py 192.168.1.1/24
# Output: Class: C, Designation: Private
def solution()-> None:
    
    #list contain type of class
    cls=["A","B","C","D","E"]

    try:
        ip = sys.argv[1]
    except:
         ip = input("Enter IP Adress like x.x.x.x/x : ")
    # Make sure the IP is Valid
    while True:
        try:
            parts=ip.split(".")
            x=int(parts[0])
            y=int(parts[1])
            z=int(parts[2])
            e=int((parts[3].split("/")[0]))
            break
        except:
                ip = input("Invalid IP Enter IP Adress with Formate x.x.x.x/x : ")
    
    i=0
    # IP Class A:	1 to 126
    # Private IP: 10.0.0.0 — 10.255.255.255
    if 1<=x<=127:
        
        if x==10:
            print(f"Class: {cls[i]}, Designation: Private")
        elif x==127 and 1<=e<=255:
            print(f"Class: {cls[i]}, Designation: special")
        else:
            print(f"Class: {cls[i]}, Designation: Public")
            
    # IP Class B:	128 to 191
    # Private IP: 172.16.0.0 — 172.31.255.255
    elif 128 <= x <= 191:
        i+=1
        if x==172 and 16<=y<=31:
            print(f"Class: {cls[i]}, Designation: Private")
        else:
            print(f"Class: {cls[1]},Designation: Public")

    # IP Class C:	192 to 223
    # Private IP: 192.168.0.0 — 192.168.255.255
    elif 192<=x<=223:
        i+=2
        if x==192 and y==168:
            print(f"Class: {cls[i]}, Designation: Private")
        else:
            print(f"Class: {cls[i]},Designation: Public")
    # IP Class D:	224 to 239  Special IP
    elif 224<=x<=239:
        i+=3
        print(f"Class: {cls[i]},Designation: special")

    # IP Class E:	240 to 255  Special IP
    elif 240<=x<=255:
        i+=4
        print(f"Class: {cls[i]},Designation: Special")
if __name__ == '__main__':
    solution()
