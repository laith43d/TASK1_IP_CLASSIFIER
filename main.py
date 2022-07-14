def IP_identifier():
    ip_adress = input('enter your IP adress in the format: x.x.x.x/x : ')
    c = ''
    Designation = ''
    y = ip_adress.split('/')
    y= y[0].split('.')
    invalid = False
    print('_______________________________')
    try:
        for i in y:
            if  isinstance(int(i),int):
                pass
        if 0 < int(y[0]) <= 127:
            c = "A"
            if int(y[0]) == 127:
                Designation = 'Special'
            elif int(y[0]) == 10:
                Designation = 'private'
            else:
                Designation = 'public'
        elif 127 < int(y[0]) <= 191:
            c = "B"
            if int(y[0]) == 172 and int(y[1]) == 16 and 0 < int(y[2]) <= 31:
                Designation = 'private'
            else:
                Designation = 'public'
        elif 191 < int(y[0]) <= 223:
            c = "C"
            if int(y[0]) == 192 and int(y[1]) == 168:
                Designation = 'private'
            else:
                Designation = 'public'
        elif 223 < int(y[0]) <= 239:
            c = "D"
            Designation = 'Special'
        elif 239 < int(y[0]) <= 255:
            c = "E"
            Designation = 'Special'
        else:
            invalid = True
            print('invalid ip')
            IP_identifier()
        if not invalid:
            print('Class: {} , Designation: {}'.format(c,Designation))
            print('_______________________________')
            again()
    except:
            print("this is not ip adress")
            print('_______________________________')
            IP_identifier()


def again():
        x = input('do you want to enter another IP ? enter Y/N  : ')
        if x == 'N' or x == 'n':
            pass
        elif x == 'Y' or x == 'y':
            IP_identifier()
        else:
            print('invalid input please choose Y or N ')
            again()

IP_identifier()