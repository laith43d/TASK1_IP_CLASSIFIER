def solution():
    a=input("Enter the IP Address:")
    b=a.split("/")
    ipA= b[0].split('.')
    ipA=[int(i) for i in ipA]
    # print(ipA)

    for j in ipA:
        if j<0 or j>255:
            print("invalid ip address")
            break



    

    if ipA[0]>=1 and ipA[0]<=126:
        # print("aaaa")
        if(ipA[0]==10):
            print("Class: A, Designation: Private")
        else:
            print("Class: A, Designation: Public")
    elif ipA[0]==127:
        print("Class: A, Designation: Special")
    elif ipA[0]>=128 and ipA[0]<=191:
        if ipA[0]== 172 and ipA[1]>=16 and ipA[1]<=31:
            print("Class: B, Designation: Private")
        else:
            print("Class: B, Designation: Public")

    elif ipA[0]>=192 and ipA[0]<=223:
        if ipA[0]== 192 and ipA[1]>=168:
            print("Class: C, Designation: Private")
        else:
            print("Class: C, Designation: Public")

    elif ipA[0]>=224 and ipA[0]<=239:
        print("Class: D, Designation: Public")
    elif ipA[0]>=240 and ipA[0]<=255:
        print("Class: E, Designation: Public")

if __name__ == '__main__':
    solution()
