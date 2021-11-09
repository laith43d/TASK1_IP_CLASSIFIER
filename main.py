import sys


def IP():

    if len(sys.argv) == 1:
         givenIP = input('\nPlease enter an IP address (IP/mask), to exit type "": ')
         try:
            ipmask = givenIP.split("/")
            split_ip = ipmask[0].split('.')

            if int(split_ip[0]) == 127 and 0 <= int(split_ip[1]) <= 255:
                print('\n IP Class A, Ip Designation: Special')
            elif 1 <= int(split_ip[0]) <= 126:
                if int(split_ip[0]) == 10:
                    print('\n IP Class A, Ip Designation: private')
                else:
                    print('\n Ip Class A, Ip Designation: public')
            elif 128 <= int(split_ip[0]) <= 191:
                if ((int(split_ip[0]) == 172) and (16 <= int(split_ip[1]) <= 31)) or ((int(split_ip[0]) == 169) and (int(split_ip[1]) == 254)):
                    print('\n Ip Class B, Ip Designation: private')
                else:
                    print('\n Ip Class B, Ip Designation: public')
            elif 192 <= int(split_ip[0]) <= 223:
                if int(split_ip[0]) == 192 and (int(split_ip[1]) == 168):
                    print('\n Ip Class C, Ip Designation: private')
                else:
                    print('\n IP Class C, Ip Designation: public')
            elif 224 <= int(split_ip[0]) <= 239:
                print('\n IP Class D, Ip Designation: Special')
            elif 240 <= int(split_ip[0]) <= 255:
                print('\n Ip Class E, Ip Designation: Special')

         except (IndexError, ValueError):
            if givenIP == 'x' or givenIP == 'X': sys.exit()
            else:
                print('\nPlease give a valid IP/MASK address in #.#.#.#/# format,' )
                
                IP()

        



if __name__ == '__main__':
    IP()