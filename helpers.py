def check_class(param):
    if 1 <= int(param[0]) <= 127:
        print('the class of ip is A')
        if int(param[0]) == 10:
            print('this ip is in the private range')
        elif int(param[0]) == 127:
            print('this ip is special')
        else:
            print('this ip is in the public range')
        # 128 to 191
    elif 128 <= int(param[0]) <= 191:
        print('the class of ip is B')
        if int(param[0]) == 172:
            if 16 <= int(param[1]) <= 31:
                print('ip in the private range')
            else:
                print('this ip is in the special range')
        elif 0 <= int(param[1]) <= 255 and (int(param[2]) == 0) and (int(param[3]) == 0):
            print('this ip is in the public range')
        else:
            print('this ip is in the special range')
    # ending of class b
    #     192 to 223
    elif 192 <= int(param[0]) <= 223:
        print('the class of ip is C')
        if int(param[0]) ==127 and int(param[3]) >=1:
            print('this ip is in the special range')
        if int(param[1]) == 168:
            print('ip in the private range')
        else:
            print('this ip is in the public range')
        #     224 to 239
    elif 224 <= int(param[0]) <= 239:
        print('the class of ip is D')
        #     240 to 254
    elif 240 <= int(param[0]) <= 254:
        print('the class of ip is E')
    else:
        print('you have missed something')
