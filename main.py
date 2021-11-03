import sys
class ipClasses(object):


    _maskList = {
        0: '0.0.0.0',
        1: '128.0.0.0',
        2: '192.0.0.0',
        3: '224.0.0.0',
        4: '240.0.0.0',
        5: '248.0.0.0',
        6: '252.0.0.0',
        7: '254.0.0.0',
        8: '255.0.0.0',
        9: '255.128.0.0',
        10: '255.192.0.0',
        11: '255.224.0.0',
        12: '255.240.0.0',
        13: '255.248.0.0',
        14: '255.252.0.0',
        15: '255.254.0.0',
        16: '255.255.0.0',
        17: '255.255.128.0',
        18: '255.255.192.0',
        19: '255.255.224.0',
        20: '255.255.240.0',
        21: '255.255.248.0',
        22: '255.255.252.0',
        23: '255.255.254.0',
        24: '255.255.255.0',

        25: '255.255.255.128',
        26: '255.255.255.192',
        27: '255.255.255.224',
        28: '255.255.255.240',
        29: '255.255.255.248',
        30: '255.255.255.252',
        31: '255.255.255.254',
        32: '255.255.255.255',
    }

    def __init__(self, givenIP=''):

        # workingValues variable initialization
        self.workingIP = [0, 0, 0, 0]
        self.workingMask = 0
        self.workingMaskInt = [0, 0, 0, 0]



        self.ipmask = givenIP.split('/')
        self.splitMask = self.ipmask[1]

        self.splitIP = self.ipmask[0].split('.')

        for index in range(len(self.splitIP)):
            self.workingIP[index] = int(self.splitIP[index])
            if self.workingIP[index] > 255: raise ValueError
            if index > 3: raise ValueError



        self.workingMask = int(self.splitMask)
        if self.workingMask > 32 or self.workingMask < 0: raise ValueError


    def Classes(self):
        self.ipClass = ''
        test = self.workingIP
        if test[0] >=1 and test[0]<=127:
            self.ipClass = 'A'

        elif test[0] >=128 and test[0]<=191:
            self.ipClass = 'B'

        elif test[0] >=192 and test[0]<=223:
            self.ipClass = 'C'

        elif test[0] >=224 and test[0]<=239:
            self.ipClass = 'D'

        elif test[0] >=240 and test[0]<=255:
            self.ipClass = 'E'

        elif test[0] <= 0:
            self.ipClass="invalid IP address"

        elif test[3] == 0:
            self.ipClass="host id  should not be 0 or less than zero "

        return self.ipClass

    def Designation(self):

        self.ipDesignation = ''
        test = self.workingIP
        if test[0] == 0 :
            self.ipDesignation = 'Internet Block'

        elif test[0] == 10 :
            self.ipDesignation = 'Internet Private Address'

        elif test[0] ==  172:
            self.ipDesignation = 'Internet Private Address - Supernetting'

        elif test[0] ==  192:
            self.ipDesignation = 'Internet Private Address - Supernetting'

        elif test[0] == 127:
            self.ipDesignation="Local Host Address"

        elif test[0] >=224 and test[0]<=239:
            self.ipDesignation = 'Reserved for multicast groups'

        elif test[0] >=240 and test[0]<=255:
            self.ipDesignation = 'Reserved for development purpose'

        elif test[0] <= 0 :
            self.ipDesignation="Invalid ip address"

        elif test[3] == 0:
            self.ipDesignation="host id  should not be 0 or less than zero "

        else:
            self.ipDesignation = 'Internet Public Address'

        return self.ipDesignation


    def output(self, givenIP):
        print(f'Class: {self.Classes()}\nDesignation:{self.Designation()} ')
        print('Finished')

def main():

        if len(sys.argv) == 1:
            givenIP = input('\nPlease give an IP address (IP/MASK), (to exit type "X"): ')
            try:
                ipAddress = ipClasses(givenIP)
                ipAddress.output(givenIP)

            except (IndexError, ValueError):
                if givenIP == 'x' or givenIP == 'X':
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
                if givenIP == 'x' or givenIP == 'X':
                    sys.exit()
                else:
                    print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format,' '\n'
                          '\tfor example: 192.168.1.1/24, or 10.10.10.1/28')


if __name__ == '__main__':
        main()
