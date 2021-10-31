import sys

class ip(object):


    _maskList = {
        0:'0.0.0.0',
        1:'128.0.0.0',
        2:'192.0.0.0',
        3:'224.0.0.0',
        4:'240.0.0.0',
        5:'248.0.0.0',
        6:'252.0.0.0',
        7:'254.0.0.0',
        8:'255.0.0.0',
        9:'255.128.0.0',
        10:'255.192.0.0',
        11:'255.224.0.0',
        12:'255.240.0.0',
        13:'255.248.0.0',
        14:'255.252.0.0',
        15:'255.254.0.0',
        16:'255.255.0.0',
        17:'255.255.128.0',
        18:'255.255.192.0',
        19:'255.255.224.0',
        20:'255.255.240.0',
        21:'255.255.248.0',
        22:'255.255.252.0',
        23:'255.255.254.0',
        24:'255.255.255.0',
        25:'255.255.255.128',
        26:'255.255.255.192',
        27:'255.255.255.224',
        28:'255.255.255.240',
        29:'255.255.255.248',
        30:'255.255.255.252',
        31:'255.255.255.254',
        32:'255.255.255.255',
        }

    def __init__(self, givenIP = ''):
        """
        """


        self.workingIP = [0, 0, 0, 0]
        self.workingMask = 0
        self.workingMaskInt = [0, 0, 0, 0]
        # ----------------------------------

        self.ipmask = givenIP.split('/')
        self.splitMask = self.ipmask[1]
        # ---------------------------------

        # Split IP segments based on '.'
        self.splitIP = self.ipmask[0].split('.')

        for index in range(len(self.splitIP)):
            self.workingIP[index] = int(self.splitIP[index])
            if self.workingIP[index] > 255: raise ValueError
            if index > 3: raise ValueError
        # --------------------------
        # Mask initialization
        self.workingMask = int(self.splitMask)
        if self.workingMask > 32 or self.workingMask < 0: raise ValueError
        if not self.workingMask:
            test = self.getClass()
            if test == 'A':
                self.workingMask = 8
            if test == 'B':
                self.workingMask = 16
            if test == 'C':
                self.workingMask = 24
            if test == 'D':
                print('Multicast Address, using /24')
                self.workingMask = 24
            if test == 'E':
                print('Reserved Address, using /24')
                self.workingMask = 24
            del test
        self.workingMaskListSplit = (self._maskList.get(self.workingMask)).split('.')
        self.workingMaskDotted = self._maskList.get(self.workingMask)
        for index in range(len(self.workingMaskListSplit)):
            self.workingMaskInt[index] = int(self.workingMaskListSplit[index])


    def representOutput(self, givenIP):
            print(givenIP)
            print('Class: {}, Designation: {}'.format(self.getClass(), self.getDesignation()))

    def getClass(self):


            self.ipClass = ''
            test = self.ipBinCalc()
            if test[0] == '0':
                self.ipClass = 'A'

            if test[:2] == '10':
                self.ipClass = 'B'

            if test[:3] == '110':
                self.ipClass =  'C'

            if test[:4] == '1110':
                self.ipClass = 'D'

            if test[:4] == '1111':
                self.ipClass = 'E'

            return self.ipClass

    def ipBinCalc(self):


        self.binIP = '{:08b}.{:08b}.{:08b}.{:08b}'.format(self.workingIP[0], self.workingIP[1],
                                                          self.workingIP[2], self.workingIP[3])

        return self.binIP

    def getDesignation(self):


        self.ipDesignation = ''
        test = self.ipBinCalc()
        if test[0] == '0' and self.workingMask == 0:
            self.ipDesignation = 'Internet Block'

        elif test[0] == '0' and self.workingIP[0] == 10 and self.workingMask >= 8:
            self.ipDesignation = 'Internet Private Address'



        elif test[0] == '0' and self.workingMask <= 8:
            self.ipDesignation = 'Internet Public Address - Supernetting'

        elif test[0] == '0' and self.workingIP[0] == 127:
            self.ipDesignation = 'Local Host Address'

        elif test[:2] == '10' and self.workingIP[0] == 172 and self.workingIP[1] == 16 and self.workingMask >= 12:
            self.ipDesignation = 'Internet Private Address'


        elif test[:3] == '110' and self.workingIP[0] == 192 and self.workingIP[1] == 168 and self.workingMask >= 16:
            self.ipDesignation =  'Internet Private Address'

        else:
            self.ipDesignation = 'Internet Public Address'

        return self.ipDesignation


def main():


    if len(sys.argv) == 1:
        givenIP = input('\nPlease give an IP address (IP/MASK), (to exit type "X"): ')
        try:
            ipAddress = ip(givenIP)
            ipAddress.representOutput(givenIP)

        except (IndexError, ValueError):
            if givenIP == 'x' or givenIP == 'X': sys.exit()
            else:
                print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format,' '\n'
                '\tfor example: 192.168.1.1/24, or 10.10.10.1/28')
                main()
    else:

        print("This version accepts only one IP address, processing the first give IP - \n")

        givenIP = sys.argv[1]
        try:
            ipAddress = ip(givenIP)
            ipAddress.representOutput(givenIP)



        except (IndexError, ValueError):
            if givenIP == 'x' or givenIP == 'X': sys.exit()
            else:
                print('\nPlease give a valid IPv4/MASK address in #.#.#.#/# format,' '\n'
                '\tfor example: 192.168.1.1/24, or 10.10.10.1/28')




if __name__ == '__main__':
    pass
    main()