import sys
count=0
def solution():

    ip = input("Enter Your Ip Please: ")
    spip = ip.split('.')
    if len(spip) == 4:
    #convert input to int
        try:
            subip1 = int(spip[0])
            subip2 = int(spip[1])
            subip3 = int(spip[2])
            x=spip[3].split('/')
            subip4 = int(x[0])
        except ValueError:
            print("You Entered an incorrect Ip, Pleas Try again")
            global count
            if count < 2:
                solution()
                count = count + 1
            else:
                print("Try agne later...")
                sys.exit()

    else:
        print("Please Enter IP in Correct way, like: xxx.xxx.xxx.xxx/xx")

        if count < 2:
            count = count + 1
            solution()
        else:
            print("Try agne later...")
            sys.exit()


    try:
        #this condition is so that the user does not enter a value greater than 255 or less than 0

        if ((subip1 > 255 or subip1 < 0) or (subip2 > 255 or subip2 < 0) or (subip3 > 255 or subip3 < 0) or (
                subip4 > 255 or subip4 < 0)):
            print("You Entered an incorrect Ip, Pleas Try again")
            if count <2:
                count = count + 1
                solution()
            else:
                print("Try agne later...")
                sys.exit()
        # check what class the ip belongs to.
        if subip1 >= 0 and subip1 <= 127:
            print("Class: A, ",end='')
        elif subip1 >= 128 and subip1 <= 191:
            print("Class: B, ",end='')
        elif subip1 >= 192 and subip1 <= 223:
            print("Class: C, ",end='')
        elif subip1 >= 224 and subip1 <= 239:
            print("Class: D, ",end='')
        elif subip1 >= 240 and subip1 <= 254:
            print("Class: E, ",end='')
        else:
            print("Wrong Value Please Enter Correct IP")
            if count < 2:
                count = count + 1
                solution()
            else:
                print("Try agne later...")
                sys.exit()

        # check IP if public or private or special
        ##conditions
        A=subip1 == 10
        B=(subip1==172 and (subip2 >= 16 and subip2 >= 31))
        C=(subip1==192 and subip2==168)
        Ap=((subip1>=1 and subip1<=9) or (subip1>=11 and subip1<=126))
        Bp=((subip1==128) or (subip1 ==172 and (subip2==15 or subip2==32)) or (subip1==191 and subip2==255 ))
        Cp=((subip1==192 and subip2 != 168) or (subip1==192 and (subip2==167 or subip2==169)) or (subip1==223) )
        Dp= subip1==224
        Ep= subip1==240



        if A or subip1==172 and B or C :
             print("Designation: Private ",)
        elif Ap or Bp or Cp or Dp or Ep:
             print("Designation: Public ")
        elif subip1==127 and subip2==0:
             print("Designation: Special ")
        else :
            print("Designation: Special ")
    except UnboundLocalError:
        pass



total = 0
def func():
    # refer to global variable 'total' inside function
    global total
    print(total)
    if total < 10:
        total = total+1
        print(total)

if __name__ == '__main__':
   pass

solution()
