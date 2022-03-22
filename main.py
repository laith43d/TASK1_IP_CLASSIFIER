from tracemalloc import stop

def private(insert):
    def_list = insert.split(".")
    if 0 <= int(def_list[0]) <= 126:
        if int(def_list[0]) in (0,127):
            print('Class: A, Designation: Special')
            return
        elif int(def_list[3].split("/",1)[0]) in (0,255):
            print('Class: A, Designation: Special')
            return
        elif int(def_list[0]) == 10:
            print('Class: A, Designation: Private')
            return
        else:
            print('Class: A, Designation: Public')
            return

    # Class A
    
    elif 128 <= int(def_list[0]) <= 191:
        if int(def_list[3].split("/",1)[0]) in (0,255):
            print('Class: B, Designation: Special')
            return
        elif int(def_list[0]) == 172 and 16 <= int(def_list[1]) <= 31:
            print('Class: B, Designation: Private')
            return
        else:
            print('Class: B, Designation: Public')
            return
        
    # Class B

    elif 192 <= int(def_list[0]) <= 223:
        if int(def_list[3].split("/",1)[0]) in (0,255):
            print('Class: C, Designation: Special')
            return
        elif int(def_list[0]) == 192 and int(def_list[1]) == 168:
            print('Class: C, Designation: Private')
            return
        else:
            print('Class: C, Designation: Public')
            return

    # Class C

    elif 224 <= int(def_list[0]) <= 239:
        print('Class: D, Designation: Special')
        return

    # Class D

    elif 240 <= int(def_list[0]) <= 254:
        print('Class: E, Designation: Special')
        return

    # Class E
    
    elif int(def_list[0]) == 255 and int(def_list[1]) == 255 and int(def_list[2]) == 255 and int(def_list[3].split("/",1)[0]) == 255:
        print('Class: E, Designation: Special')
        return
    
    # Special 255.255.255.255

    elif int(def_list[0]) == 127:
        print('Class: none, Designation: Special')
        return
    
    # none 127.x.x.x

def solution():
    insertion = input('Please Insert IP Address: ')
    private(insertion)

solution()

if __name__ == '__main__':
    pass
