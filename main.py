def solution():

    # promote user for input
    ipadress=input("please enter IP adress: ")
    ipmask = ipadress.split("/")

    # split ip adress when reaching a dot (.)
    ipclasses = ipmask[0].split('.')

    # typecasting list into integer to perform operations
    ipclasses=[int(i) for i in ipclasses]

    # validate ip adress
    ipvalidation = len(ipclasses)

    # ------------------------------------------------------------------------
    if ipvalidation !=4:
        print("your ip adress is invalid!")
    else:

        if ipclasses[0]>=1 and ipclasses[0]<=127:
# class A 
            if ipclasses[0]==10:
                print("Class: A || Designation: Private")
            elif ipclasses[0] == 1 and ipclasses[3] >=1:
                print ("Class A || Designation: Public")
            else:
                print("Class: A || Designation:  Special")





# class B

        elif ipclasses[0]>=128 and ipclasses[0]<=191:
            if ipclasses[0] == 172 and 16 <= ipclasses[1] <= 32:
                print("Class: B || Designation:  Private")
            else :
                print ("Class: B || Designation:  public")
            

            




# class C
        elif ipclasses[0]>=192 and ipclasses[0]<=223:
            if ipclasses[0]== 192 and ipclasses[1]>=168:
                print("Class: C ||  Designation:  private")
            else:
                print("Class: C ||  Designation:  public")


 

# class D
        elif ipclasses[0]>=224 and ipclasses[0]<=239:
            print("Class: D ||  Designation: Special")
# class E

        elif ipclasses[0]>=240 and ipclasses[0]<=255:
            print("Class: E ||  Designation: Special")




if __name__ == '__main__':
    solution()


