def solution(ip):

    try1 = '\nPlease give a valid IPv4 address in #.#.#.# format,' '\n''     for example: 192.168.1.1, or 10.10.10.1'''

    try:

        first = ip.index('.')
        first1 = ip[:first]
        index1 = first + 1

        Second = ip[index1:]
        Second2 = Second.index('.')
        Second3 = Second[:Second2]
        Third = Second.index('.')
        Third2 = Third + 1

        Third1 = Second[Third2:]
        s1 = Third1.index('.')
        Third3 = Third1[:s1]
        ipa1 = int(first1)
        ipa2 = int(Second3)
        ipa3 = int(Third3)

        bin1 = format(ipa1, "08b")

        if ipa1 < 256 and ipa2 < 256 and ipa3 < 256:
            if bin1[0] == '0':
                class1 = 'A'
            if bin1[:2] == '10':
                class1 = 'B'

            if bin1[:3] == '110':
                class1 = 'C'

            if bin1[:4] == '1110':
                class1 = 'D'

            if bin1[:4] == '1111':
                class1 = 'E'

            if ipa1 == 10:
                ipDesignation = 'Private'

            elif ipa1 == 172 and ipa2 >= 16 and ipa2 <= 31:
                ipDesignation = 'Private'

            elif ipa1 == 192 and ipa2 == 168:
                ipDesignation = 'Private '

            elif ipa1 >= 224 and ipa1 <= 239:
                ipDesignation = 'Special'

            elif ipa1 >= 240 and ipa1 <= 255:
                ipDesignation = 'Special'
            elif ipa1 == 127:
                ipDesignation = 'Special'

            else:
                ipDesignation = 'Public '

            print()
            print('|', 20 * "-", "IP Address", 20 * "-", '|')
            print()
            print()
            print('           Class: {} , Designation: {}              '.format(
                class1, ipDesignation))
            print()
            print()
            print('|', 20 * "-", "IP Address", 20 * "-", '|')

        else:
            print("   ------------------------------------------")
            print("       The IP Address OUT OF THE RANGE     ")
            print("   ------------------------------------------")
            X = input("Enter 'X' to try again  OR any key to EXIT: ")
            if X == 'x' or X == 'X':
                
                print()
                print()
                print("-------------------------------------------------------------------------")
                print()
                print()
                s = input("Enter The IP Address: ")
                solution(s)
            
            else:
                
                exit()
            
            

    except:
        print(try1)

        print()

        X = input("Enter 'X' to try again  OR any key to EXIT: ")
        if X == 'x' or X == 'X':
            print()
            print()
            print(
                "-------------------------------------------------------------------------")
            print()
            print()
            s = input("Enter The IP Address: ")
            solution(s)
        else:
            exit()


print("-------------------------------------------------------------------------")
print()
print()
s = input("Enter The IP Address: ")
solution(s)
if __name__ == '__main__':
    pass
