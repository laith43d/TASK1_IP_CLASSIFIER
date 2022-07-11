import sys
# Print the Class and Designation of IP Address
# Classes: A, B, C, D, E
# Designation: Private, Public, Special
# Run: python main.py 192.168.1.1/24
# Output: Class: C, Designation: Private
def solution()-> None:

    try:
        ip = sys.argv[1]
    except:
         ip = input("Enter IP Adress like x.x.x.x/x : ")
    # Make sure the IP is Valid
    while True:
        try:
            parts=ip.split(".")
            part1=int(parts[0])
            part2=int(parts[1])
            part3=int(parts[2])
            part4=int((parts[3].split("/")[0]))
            break
        except:
                ip = input("Invalid IP Enter IP Adress with Formate x.x.x.x/x : ")
    class_name = "Invalid"
    designation = "public"
    # IP Class A:	1 to 126
    # Private IP: 10.0.0.0 — 10.255.255.255
    if 1<=part1<=127:
        class_name="A"
        if part1==10:
            designation="Private"
            print(f"Class: {class_name}, Designation: {designation}")
        #here class A is Special when part1 =127 and part2 between 1 to 255
        elif part1==127 and 1<=part4<=255:
            designation="Special"
            print(f"Class: {class_name}, Designation: {designation}")
        else:
            print(f"Class: {class_name}, Designation: {designation}")
            
    # IP Class B:	128 to 191
    # Private IP: 172.16.0.0 — 172.31.255.255
    elif 128 <= part1 <= 191:
        class_name="B"
        if part1==172 and 16<=part2<=31:
            designation="Private"
            print(f"Class: {class_name}, Designation: {designation}")
        else:
            print(f"Class: {class_name}, Designation: {designation}")

    # IP Class C:	192 to 223
    # Private IP: 192.168.0.0 — 192.168.255.255
    elif 192<=part1<=223:
        class_name="C"
        if part1==192 and part2==168:
            designation="private"
            print(f"Class: {class_name}, Designation: {designation}")
        else:
            print(f"Class: {class_name}, Designation: {designation}")

    # IP Class D:	224 to 239  Special IP
    elif 224<=part1<=239:
        class_name="D"
        designation="Special"
        print(f"Class: {class_name}, Designation: {designation}")

    # IP Class E:	240 to 255  Special IP
    elif 240<=part1<=255:
        class_name="E"
        designation="Special"
        print(f"Class: {class_name}, Designation: {designation}")
if __name__ == '__main__':
    solution()
