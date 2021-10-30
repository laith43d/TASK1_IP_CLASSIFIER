


class ipCalcMainClass(object):
    def __init__(self, givenIP=''):
        self.workingIP = [0, 0, 0, 0]
        self.workingMask = 0

        self.ipmask = givenIP.split('/')
        self.splitMask = self.ipmask[1]
        self.splitIP = self.ipmask[0].split('.')

        self.x = ''
        # special
        if self.splitIP[0] == '127' and (0 <= int(self.splitIP[1]) <= 255) and (
                0 <= int(self.splitIP[2]) <= 255) and (
                1 <= int(self.splitIP[3]) <= 255):
            self.x = 'Class A, Special'
        # class A
        elif self.splitIP[0] == '10' and (0 <= int(self.splitIP[1]) <= 255):
            self.x = 'Class A, Private'
        elif 1 <= int(self.splitIP[0]) <= 127:
            self.x = 'Class A, Public'

        # class B
        elif self.splitIP[0] == '169' and self.splitIP[1] == '254' and (
                0 <= int(self.splitIP[2]) <= 255) and (
                0 <= int(self.splitIP[3]) <= 255):
            self.x = 'Class B, APIPA '
        elif self.splitIP[0] == '172' and (31 >= int(self.splitIP[1]) >= 16):
            self.x = 'Class B, Private'
        elif 172 <= int(self.splitIP[0]) <= 191:
            self.x = 'Class B, Public'

        # class C
        elif self.splitIP[0] == '192' and self.splitIP[1] == '168':
            self.x = 'Class C, Private'
        elif 192 <= int(self.splitIP[0]) <= 223:
            self.x = 'Class C, Public'
        # class D
        elif 224 <= int(self.splitIP[0]) <= 239:
            self.x = 'Class D'

        # class E
        elif 240 <= int(self.splitIP[0]) <= 255:
            self.x = 'Class E'

        else:
            self.x = ' Unknown'


ip = ipCalcMainClass
givenIP = input('\nPlease give an IP address (IP/MASK): ')
ipAddress = ip(givenIP).x
print(ipAddress)

