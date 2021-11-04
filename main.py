import sys

class ipClasses(object):
    def __init__(self, givenIP=''):
        self.workingIP = [0, 0, 0, 0]
        self.workingMask = 0

        self.ipmask = givenIP.split('/')
        self.splitMask = self.ipmask[1]
        self.splitIP = self.ipmask[0].split('.')

        self.theip = ''
        # special
        if self.splitIP[0] == '127' and (0 <= int(self.splitIP[1]) <= 255) and (
                0 <= int(self.splitIP[2]) <= 255) and (
                1 <= int(self.splitIP[3]) <= 255):
            self.theip = 'Class A, Special'
        # class A
        elif self.splitIP[0] == '10' and (0 <= int(self.splitIP[1]) <= 255):
            self.theip = 'Class A, Private'
        elif 1 <= int(self.splitIP[0]) <= 127:
            self.theip = 'Class A, Public'

        # class B
        elif self.splitIP[0] == '169' and self.splitIP[1] == '254' and (
                0 <= int(self.splitIP[2]) <= 255) and (
                0 <= int(self.splitIP[3]) <= 255):
            self.theip = 'Class B, Special '
        elif self.splitIP[0] == '172' and (31 >= int(self.splitIP[1]) >= 16):
            self.theip = 'Class B, Private'
        elif 172 <= int(self.splitIP[0]) <= 191:
            self.theip = 'Class B, Public'

        # class C
        elif self.splitIP[0] == '192' and self.splitIP[1] == '168':
            self.theip = 'Class C, Private'
        elif 192 <= int(self.splitIP[0]) <= 223:
            self.theip = 'Class C, Public'
        # class D
        elif 224 <= int(self.splitIP[0]) <= 239:
            self.theip = 'Class D'

        # class E
        elif 240 <= int(self.splitIP[0]) <= 255:
            self.theip = 'Class E'

        else:
            self.theip = ' Unknown IP try something valid'
    def output(self, givenIP):
        ipAddress = ipClasses(givenIP).theip
        print(ipAddress)


def main():

        if len(sys.argv) == 1:
            givenIP = input('\nPlease give an IP address (IP/MASK), (to exit type "exit"): ')
            try:
                ipAddress = ipClasses(givenIP)
                ipAddress.output(givenIP)

            except (IndexError, ValueError):
                if givenIP == 'exit' or givenIP == 'Exit':
                    sys.exit()
                else:
                    print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format,' '\n'
                          '\tfor example: 192.168.1.1/24, or 10.10.10.1/28')
                    main()
        else:
            print("This version accepts only one IP address, processing the first give IP - \n")
            givenIP = sys.argv[1]
            try:
                ipAddress = ipClasses(givenIP)
                ipAddress.output(givenIP)


            except (IndexError, ValueError):
                if givenIP == 'exit' or givenIP == 'Exit':
                    sys.exit()
                else:
                    print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format,' '\n'
                          '\tfor example: 192.168.1.1/24, or 10.10.10.1/28')


if __name__ == '__main__':
        main()

