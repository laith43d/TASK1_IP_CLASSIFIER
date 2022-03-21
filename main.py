from tracemalloc import stop

def private(insert):
    def_list = insert.split(".")
    if int(def_list[3].split("/",1)[0]) in (0,255):
        print('Reserved')
        return
    elif int(def_list[0]) == 255 and int(def_list[1]) == 255 and int(def_list[2]) == 255 and int(def_list[3].split("/",1)[0]) == 255:
        print('Reserved')
        return
    elif int(def_list[0]) == 10:
        print('local')
        return
    elif int(def_list[0]) in (127,0):
        print('Reserved')
        return
    elif int(def_list[0]) == 172 and 16 <= int(def_list[1]) <= 31:
        print('Local')
        return
    elif int(def_list[0]) == 192 and int(def_list[1]) == 168:
        print('Local')
        return
    elif 224 <= int(def_list[0]) <= 254:
        print('Reserved')
        return
    else:
        print('Public')
        return
def solution():
    insertion = input('Please Insert IP Address: ')
    private(insertion)

solution()

if __name__ == '__main__':
    pass
