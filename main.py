class IpInfo:
    def __init__(self, ip: str = None):
        split_ip = ip.split('/')
        if len(split_ip) < 2:
            raise ValueError
        subnet = split_ip[1]
        ip_parts = split_ip[0].split('.')

        if len(ip_parts) != 4:
            raise ValueError
        if int(subnet) > 32:
            raise ValueError

        self.ip_first_part = ip_parts[0]
        self.ip_second_part = ip_parts[1]
        self.ip_third_part = ip_parts[2]
        self.ip_fourth_part = ip_parts[3]
        self.Class = ''
        self.des = ''

    def get_ip_info(self):
        if self.ip_first_part == '10':
            self.Class = 'A'
            self.des = 'Private'

        elif self.ip_first_part == '172' and 16 <= int(self.ip_second_part) <= 31:
            self.Class = 'B'
            self.des = 'Private'

        elif self.ip_first_part == '192' and self.ip_second_part == '168':
            self.Class = 'C'
            self.des = 'Private'

        elif self.ip_first_part == '192' or 173 <= int(self.ip_first_part) < 224:
            self.Class = 'C'
            self.des = 'Public'

        elif self.ip_first_part == '172' or 173 <= int(self.ip_first_part) <= 171:
            self.Class = 'B'
            self.des = 'Public'

        elif self.ip_first_part == '127':
            self.Class = 'A'
            self.des = 'Special'

        elif 1 < int(self.ip_first_part) <= 126:
            self.Class = 'A'
            self.des = 'Public'

        elif 255 >= int(self.ip_first_part) >= 224:
            self.Class = 'D or E'
            self.des = 'Special'

        else:
            raise ValueError

        return f'The Class is => {self.Class} \nand The designation is => {self.des}'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_ = input('Enter an ip address => x.x.x.x/x\n')
    try:
        info = IpInfo(input_)
        print(info.get_ip_info())
    except ValueError:
        print('Enter a address in this format => x.x.x.x/x')
