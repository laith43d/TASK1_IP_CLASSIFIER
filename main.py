import sys 
#solution function to call the toher functions that we made 
def solution():
    ip_split = check_validity()
    classification(ip_split)



#function to check the validity of ip address and returns the ip  that we splited from its mask 
def check_validity():

    ip_address = input('please enter your ip address in this form "x.x.x.x/x" ')
    ip, mask = ip_address.split('/')
    ip_split = ip.split('.')

    if len(ip_split) !=4:

        print('invalid ip address .. please try by typing this way "x.x.x.x/x"  ')

    ip_split = [int(i) for i in ip_split]


    for i in ip_split:
        if 0 <= i <= 255:
            pass
        else:
            print('please try again ')
            sys.exit(1)
    return ip_split


#function to determind the class and designation of the ip address

def classification(ip_split : list):

    try:

        if (ip_split[0]) == 127 and 0 <= (ip_split[1]) <= 255:
            print('class A , special')
        elif  0 <= (ip_split[0]) <= 126:
            if ip_split[0] == 10:
                print('class A ,  private')
            else:
                print('class A ,  public')

        elif 128 <= ip_split[0] <= 191:

            if (((ip_split[0]) == 172) and ( 16 <= ip_split[1] <= 31)) or (((ip_split[0]) == 169) and ((ip_split[0]) == 254)):

                print('class B , private')
            else:
                print('class B ,  public')
        elif 192 <= (ip_split[0]) <= 223:
            if ((ip_split[0]) == 192 and (ip_split[1]) == 168):
                print('class c ,  private')
            else:
                print('class c ,  public')
        elif 224 <= (ip_split[0]) <= 239:
            print('class D , special')
        elif  240 <= (ip_split[0]) <= 225:
            print('class E ,  special')

    except ValueError:

        if ip_split == 'x' or ip_split == 'X':
            sys.exit(1)
        else:
            print('please try again and type it into this form "x.x.x.x/x" ')




# condition to execute this module only 
if __name__ == "__main__":

    solution()



