class HassanAli:

    def __init__(self, give_ip: str = None):
        ip_subnet = give_ip.split('/')
        if len(ip_subnet) < 2:
            raise ValueError

        ip = ip_subnet[0]

        subnet = ip_subnet[1]

        ip_dotted = ip.split('.')

        if len(ip_dotted) != 4:
            raise ValueError

        if int(subnet) > 32:
            raise ValueError

        self.ip_dotted = ip_dotted
        self.class_: str = ''
        self.designation: str = ''

    def kill_it(self):

        if self.ip_dotted[0] == '10':
            self.class_ = 'A'
            self.designation = 'Private'

        elif self.ip_dotted[0] == '172' and 16 <= int(self.ip_dotted[1]) <= 31:
            self.class_ = 'B'
            self.designation = 'Private'

        elif self.ip_dotted[0] == '192' and self.ip_dotted[1] == '168':
            self.class_ = 'C'
            self.designation = 'Private'

        elif self.ip_dotted[0] == '192' or 173 <= int(self.ip_dotted[0]) < 224:
            self.class_ = 'C'
            self.designation = 'Public'

        elif self.ip_dotted[0] == '172' or 128 <= int(self.ip_dotted[0]) <= 171:
            self.class_ = 'B'
            self.designation = 'Public'

        elif self.ip_dotted[0] == '127':
            self.class_ = 'A'
            self.designation = 'Special'

        elif 1 < int(self.ip_dotted[0]) <= 126:
            self.class_ = 'A'
            self.designation = 'Public'

        elif 224 <= int(self.ip_dotted[0]) <= 255:
            self.class_ = 'D or E'
            self.designation = 'Special'
        else:
            raise ValueError
        return f'class: {self.class_}, designation: {self.designation}'

if __name__ == '__main__':
    i = input('Please enter an ip address: ')
    try:
        solution = HassanAli(i)
        print(solution.kill_it())
    except ValueError:
        print('Please enter a valid address in this format: x.x.x.x/x')
