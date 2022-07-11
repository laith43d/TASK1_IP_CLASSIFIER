def solution(ip):

    try1 = '\nPlease give a valid IPv4 address in #.#.#.# format,' '\n''\tfor example: 192.168.1.1, or 10.10.10.1''\n''\t       ''**and RUN the program**'

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
    except:
        print(try1)

    try:
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

    except:
        print("")

    ###########################

    try:
        if ipa1 == 10:

            ipDesignation = 'Private'

        elif ipa1 == 172 and ipa2 >= 16 and ipa2 < 32:
            ipDesignation = 'Private'

        elif ipa1 == 192 and ipa2 == 168:
            ipDesignation = 'Private '

        elif ipa1 == 127:
            ipDesignation = 'Special'

        else:
            ipDesignation = 'Public '

    ##############################

        print()
        print('|', 20 * "-", "IP Address", 20 * "-", '|')
        print('|', 52 * ' ', '|')
        print('|', 52 * ' ', '|')
        print('|          Class: {} , Designation: {}             |'.format(
            class1, ipDesignation))
        print('|', 52 * ' ', '|')
        print('|', 52 * ' ', '|')
        print('|', 20 * "-", "IP Address", 20 * "-", '|')
    except:
        print(" ")


s = input("Enter The IP Address: ")
solution(s)
if __name__ == '__main__':
    pass
