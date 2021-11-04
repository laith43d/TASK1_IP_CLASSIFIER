import sys


def solution():
    pass


if __name__ == '__main__':
    pass


class ipCalcMain(object):
    def __init__(self, givenIP=''):
        self.workingIP = [0, 0, 0, 0]
        self.workingMask = 0

        self.ipmask = givenIP.split('/')
        self.splitMask = self.ipmask[1]
        self.splitIP = self.ipmask[0].split('.')

        self.x = ''

        # special
        if self.splitIP[0] == '127':
            self.x = 'special'

        # class a
        elif 1 <= int(self.splitIP[0]) <= 126:
            if self.splitIP[0] == '10' and (0 <= int(self.splitIP[1]) <= 255):
                self.x = 'Class A, Private'
            else:
                self.x = 'Class A, Public'

        # class B
        elif 128 <= int(self.splitIP[0]) <= 191:
            if self.splitIP[0] == '172' and (16 <= int(self.splitIP[1]) <= 31):
                self.x = 'Class B, Private'
            elif self.splitIP[0] == '169' and (self.splitIP[1] == '254'):
                self.x = 'Class B, Private APIPA'
            else:
                self.x = 'Class B, Public'

        # class C
        elif 192 <= int(self.splitIP[0]) <= 223:
            if self.splitIP[0] == '192' and (self.splitIP[1] == '168'):
                self.x = 'Class C, Private'
            else:
                self.x = 'Class C, Public'
        # class D
        elif 224 <= int(self.splitIP[0]) <= 239:

            self.x = 'Class D'
        # class E
        elif 240 <= int(self.splitIP[0]) <= 255:

            self.x = 'Class E'
        else:
            self.x = 'unknown'


IpInput = sys.argv[1]
print(ipCalcMain(IpInput).x)
