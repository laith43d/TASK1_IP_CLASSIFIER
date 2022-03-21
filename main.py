def solution(get_ip):
    '''
    In This Finction return the class of ip and the Designation 
    
    '''
    get_split=get_ip.split('/')
    a= get_split[0].split('.')
    if  get_split[0] == '0.0.0.0':
        print("Designation: Private")
    elif int(a[0]) < 128:
        print("class: A")
        if int(a[0]) == 10:
            print("Designation: Private")
        elif  get_split[0] == '127.0.0.1':
            print("Designation: Speical")
        else:
            print("Designation: Puplic")
    elif int(a[0]) >= 128 and int(a[0]) < 192:
        print("Class B")
        if int(a[0]) == 172 and int(a[1])>=16 and int(a[1])<=31:
            print(",Designation: Privat")
        else:
            print("Designation: Puplic")
    elif int(a[0]) >= 192 and int(a[0]) < 224:
        print("Class: C")
        if int(a[0]) == 192 and int(a[1])==168:
            print(",Designation: Private")
        else:
            print("Designation: Puplic")
    elif int(a[0]) >= 224 and int(a[0]) < 240:
        print("Class: D , Designation: speical")
    elif int(a[0]) >= 240 and int(a[0]) <= 255:
        print("Class E ,Designation: speical")
if __name__ == '__main__':
    _ip=input("Pleace Enter Ip: ")
    solution(_ip)
