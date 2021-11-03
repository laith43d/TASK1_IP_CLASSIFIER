import sys


def IpClassifier():

    if len(sys.argv) == 1:
         givenIP = input('\nPlease give an IP address (IP/MASK), (to exit type ""): ')
         try:
            ipmask = givenIP.split("/")
            split_ip = ipmask[0].split('.')

            if int(split_ip[0]) == 127 and 0 <= int(split_ip[1]) <= 255:
                print('\nClass A, Designation: Special')
            elif 1 <= int(split_ip[0]) <= 126:
                if int(split_ip[0]) == 10:
                    print('\nClass A, Designation: private')
                else:
                    print('\nClass A, Designation: public')
            elif 128 <= int(split_ip[0]) <= 191:
                if ((int(split_ip[0]) == 172) and (16 <= int(split_ip[1]) <= 31)) or ((int(split_ip[0]) == 169) and (int(split_ip[1]) == 254)):
                    print('\nClass B, Designation: private')
                else:
                    print('\nClass B, Designation: public')
            elif 192 <= int(split_ip[0]) <= 223:
                if int(split_ip[0]) == 192 and (int(split_ip[1]) == 168):
                    print('\nClass C, Designation: private')
                else:
                    print('\nClass C, Designation: public')
            elif 224 <= int(split_ip[0]) <= 239:
                print('\nClass D,Designation: Special')
            elif 240 <= int(split_ip[0]) <= 255:
                print('\nClass E, Designation: Special')

         except (IndexError, ValueError):
            if givenIP == 'x' or givenIP == 'X': sys.exit()
            else:
                print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format,' '\n'
                '\tfor example: 192.168.1.1/24, or 10.10.10.1/28')
                IpClassifier()
         finally:
             print('\nWhy does Python live on land' '\nBecause it is above C level')
        



if __name__ == '__main__':
    IpClassifier()