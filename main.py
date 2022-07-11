def solution(ip_adress):
    c = ''
    Designation = ''
    y = ip_adress.split('.')
    invalid = False
    try:
        for i in y:
            if  isinstance(int(i),int):
                pass
        if int(y[0]) > 0 and int(y[0]) <= 127:
            c = "A"
            if int(y[0]) == 127:
                Designation = 'Special'
            elif int(y[0]) == 10:
                Designation = 'private'
            else:
                Designation = 'public'
        elif int(y[0]) > 127 and int(y[0]) <= 191:
            c = "B"
            if int(y[0]) == 172 and int(y[1]) == 16 and int(y[2]) <= 31:
                Designation = 'private'
            else:
                Designation = 'public'
        elif int(y[0]) > 191 and int(y[0]) <= 223:
            c = "C"
            if int(y[0]) == 192 and int(y[0]) == 168:
                Designation = 'private'
            else:
                Designation = 'public'
        elif int(y[0]) > 223 and int(y[0]) <= 239:
            c = "D"
            Designation = 'Special'
        elif int(y[0]) > 239 and int(y[0]) <= 255:
            c = "E"
            Designation = 'Special'
        else:
            invalid = True
            print('invalid ip')
        if not invalid:
            print('Class: {} , Designation: {}'.format(c,Designation))
    except:
            print("this is not ip adress")
#test1
solution('127.40.0.88')
print('_______________________________')
#test2
solution('15.T.0.M')
print('_______________________________')
#test3
solution('0.168.0.88')
print('_______________________________')
#test4
solution('172.16.31.88')
print('_______________________________')
#test5
solution('192.167.31.88')