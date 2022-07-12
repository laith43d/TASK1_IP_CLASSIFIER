def solution(givenIP=''):

    # Declearing the varibles and spilting the dots and slashes

    ipmask = givenIP.split('/')
    ip = ipmask[0].split('.')
    firstDigits = (int(ip[0]))
    secondtDigits = (int(ip[1]))
    thirdtDigits = (int(ip[2]))
    fourthtDigits = (int(ip[3]))

    # ________________________________________________________________

    # condtioning the numbers bases on the enterd vaule
    if firstDigits > 255 and secondtDigits > 255 and thirdtDigits > 255 and fourthtDigits > 255:
        print("Error")
    if firstDigits >= 1 and firstDigits <= 127:
        ipClass = 'A'
        designation = 'Pubilc'
        if firstDigits == 10:
            designation = 'Private'
    elif firstDigits >= 128 and firstDigits <= 191:
        ipClass = 'B'
        designation = 'Private'
        if secondtDigits >= 16 and secondtDigits <= 31:
            designation = 'Private'
    elif firstDigits >= 192 and firstDigits <= 223:
        ipClass = 'C'
        designation = 'Private'
        if thirdtDigits and fourthtDigits >= 0 and thirdtDigits and fourthtDigits <= 255:
            designation = 'Private'
    elif firstDigits >= 224 and firstDigits <= 239:
        ipClass = 'D'
        designation = 'Private'
    elif firstDigits >= 240 and firstDigits <= 255:
        ipClass = 'E'
        designation = 'Private'
    # handle if the values are not in the range
    else:
        print("Invalied input")
    # ________________________________________________________________

    # printing the values
    print("Class: {} , Designation: {}".format(ipClass, designation))


if __name__ == '__main__':

    # handling any error input
    try:
        ip = input("Enter IP ADDRESS: ")
        solution(ip)
    except ValueError:
        print("Sorry, You have enterd a wrong vaule, please try again")
