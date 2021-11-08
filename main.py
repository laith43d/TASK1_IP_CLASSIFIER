class IpClassifier:
    def __init__(self, address):
        ip = address.split('.')
        self.ip = ip

    def get_class(self):
        if self.ip[0] == '10':
            self.ip_class = 'A'
            self.designation = 'Private'

        elif self.ip[0] == '172' and 16 <= int(self.ip[1]) <= 31:
            self.ip_class = 'B'
            self.designation = 'Private'

        elif self.ip[0] == '192' and self.ip[1] == '168':
            self.ip_class = 'C'
            self.designation = 'Private'

        elif self.ip[0] == '192' or 173 <= int(self.ip[0]) < 224:
            self.ip_class = 'C'
            self.designation = 'Public'

        elif self.ip[0] == '172' or 128 <= int(self.ip[0]) <= 171:
            self.ip_class = 'B'
            self.designation = 'Public'

        elif self.ip[0] == '127':
            self.ip_class = 'A'
            self.designation = 'Special'

        elif 1 < int(self.ip[0]) <= 126:
            self.ip_class = 'A'
            self.designation = 'Public'

        elif 224 <= int(self.ip[0]) <= 255:
            self.ip_class = 'D or E'
            self.designation = 'Special'

        else:
            raise ValueError

        return f'ip_address class type: {self.ip_class},ip_address designation: {self.designation}'


if __name__ == '__main__':
    try:
        input1 = input('Please enter an ip address: x.x.x.x\n')
        ip_classifier = IpClassifier(input1)
        print(ip_classifier.get_class())
    except ValueError:
        print("please enter a valid ip address")