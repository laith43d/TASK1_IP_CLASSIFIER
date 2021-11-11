classA_public = [1, 127]
classA_private = [10, 10]

classB_public = [128, 191]
classB_private = [172, 172]

classC_public = [192, 223]
classC_private = [192, 192]

classD = [224, 239]
classE = [240, 255]

special = [127, 127]


def get_class_and_ip(data):
    ip_list = data.split('.')
    first_octet = int(ip_list[0])
    if first_octet in classA_public:
        if first_octet in classA_private:
            return 'class A , designation Private'
        elif first_octet in special:
            return 'class A , designation special'
        else:
            return 'class A , designation Public'

    elif first_octet in classB_public:
        if first_octet in classB_private:
            return 'class B , designation Private'
        else:
            return 'class B , designation Public'

    elif first_octet in classC_public:
        if first_octet in classC_private:
            return 'class C , designation Private'
        else:
            return 'class C , designation Public'

    elif first_octet in classD:
        return 'class D , designation Public'

    elif first_octet in classE:
        return 'class E , designation Public'

    else:
        return 'No Data'


def demo():
    if 127 in classA_public:
        print('class A public')
    else:
        print('fuck')


print('Welcome to IP Calculator')
print('Press Q or q for quit')

while(True):
    inputData = input('Enter IP Address:')
    if inputData == 'q' or inputData == 'Q':
        break
    else:
        print(get_class_and_ip(inputData))
