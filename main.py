#function to check the IP if it have more than one condition in many parts of ID

def seconde_check_list(start , end , ip):
    check_list = []
    for i in range(start , end ):
        check_list.append(str(i))
    if ip in check_list:
        return True
    else:
        return False


#main classes (A , B , C , D , E):

def it_class_A(ip):
    check_list = []
    for i in range(1 , 128):
        check_list.append(str(i))
    if ip[0] in check_list :
        return True
    else:
        return False
    #check the IP if it begin with range(1 , 127) class(A)

def it_class_B(ip):
    check_list = []
    for i in range(128 , 192):
        check_list.append(str(i))
    if ip[0] in check_list:
        return True
    else:
        return False
    #check the IP if it begin with range(128 , 191) class(B)

def it_class_C(ip):
    check_list = []
    for i in range(192 , 224):
        check_list.append(str(i))
    if ip[0] in check_list or class_C_spical(ip)==True:
        return True
    else:
        return False
    #check the IP if it begin with range(192 , 223) class(C)

def it_class_D(ip):
    check_list = []
    for i in range(224 , 240):
         check_list.append(str(i))
    if ip[0] in check_list:
        return True
    else:
        return False
    #check the IP if it begin with range(224 , 239) class(D)

def it_class_E(ip):
    check_list = []
    for i in range(239 , 256):
        check_list.append(str(i))
    if ip[0] in check_list:
        return True
    else:
        return False
    #check the IP if it begin with range(239 , 255)
#end of main classes of IP


#types of class-A
def class_A_public(ip):
    check_list = []
    for i in range(1,128):
        check_list.append(str (i))
    if ip[0] in check_list and ip[1:4] =='0':
        return True
    else:
        return False
    #it is public , if it start in range (1,127) and the remaining parts equal zero
def class_A_private(ip):
    check_list = []
    for i in range(0 , 256):
        check_list.append(str(i))
    if ip[0] == '10' and (ip[1] and ip[2] and ip[3]) in check_list:
        return True
    else:
        return False
    #it is private , if it start with 10 and the remaining parts in range(0,255)
#end of class-A types...


#class-B types:
def class_B_public(ip):
    check_list = []
    for i in range (128 , 192):
        check_list.append(str(i))     #seconde_check_list(start , end , part of ip)
    if ip[0] in check_list and seconde_check_list(0 ,256 , ip[1]) ==True:
        if ip[2] == '0' and ip[3] =='0':
            return True
    else:
        return False
    """if the first part of IP in range(128 , 192),
       if the second part of ip in range(0,255),
       and the ramaining equal zero,
       it will be (class-B public)"""

def class_B_private(ip):
    check_list = []
    for i in range(16 , 33):
        check_list.append(str(i))
    if ip[0] == '172' and (ip[1] in check_list):
        if (seconde_check_list(0,256,ip[2]) and seconde_check_list(0,256,ip[3])) == True:
            return True
        else:
            return False
    """if the first part of IP eqal 172
       if the second part of IP in range(16,32)
       and the remaining parts in range(0,255),
       it will be (class-B private)"""
#end of class-B types


#class - C types:
def class_C_public(ip):
    check_list = []
    for i in range(192 , 224):
        check_list.append(str(i))
    if ip[0] in check_list and ip[3] == '0':
        if (seconde_check_list(0,256,ip[1]) and seconde_check_list(0,256,ip[2])) ==True:
            return True 
    else:
        return False
    """if the first part of IP in range(192 , 224)
       if the second and third part of IP in range(0,255)
       if the last part of IP equal zero
       it will be (public)"""

def class_C_private(ip):
    check_list = []
    for i in range(0 , 256):
        check_list.append(str(i))
    if ip[0] == '192' and ip[1] =='168':
        if (ip[2] in check_list) and (ip[3] in check_list):
            return True
    else:
        return False
    """if the first part of IP equal 192,
       if the second part of IP equal 168
       and the remaining parts of IP in range(0,255)"""


#main function to find the class and type of IP
def solution(ip):
    ip_list = ip.split(".")         #split the ip where the '.' found 
    if it_class_A(ip_list) == True:
        print("class-A" , end = "  ")
        if class_A_private(ip_list) == True:
            print("private")
        elif class_A_public(ip_list) == True:
            print("public")
        else:
            print("special")
    
    elif it_class_B(ip_list) == True:
        print("class-B" , end = "  ")
        if class_B_private(ip_list) == True:
            print("private")
        elif class_B_public(ip_list) == True:
            print("public")
        else:
            print("special")
    
    elif it_class_C(ip_list) == True:
        print("class-C" , end="   ")
        if class_C_private(ip_list) ==True:
            print("private")
        elif class_C_public(ip_list) == True:
            print("public")
        else:
            print("special")

    elif it_class_D(ip_list) == True:
        print("class-D")
    elif it_class_E(ip_list) == True:
        print("class-E")

if __name__ == '__main__':
    ip = input("enter the ip address:")
    for i in ip:
        if i =="/":
            find_sub_mask = ip.index(i)    #find the index of '/' to remove submask from IP
            ip = ip[0:find_sub_mask]
    solution(ip)
    