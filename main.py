import re
import sys

""" 
Just for simplicity I have ignored some cases that cause exceptions.
"""


class IPCalculator:
    ip_class: str = 'Unknown'
    ip_designation: str = 'Unknown'
    is_valid_id: bool = False

    def __init__(self, ip):
        self.input_ip = ip
        # Trim the IP & split it by '/'
        self.ip_mask = self.input_ip.strip().split("/")
        # Take the first part of IP
        self.ip = self.ip_mask[0]
        # Split it by 'dot' to four octets each one as integer.
        self.octets = [int(x) for x in self.ip.split(".")]
        # Validation
        self.check_validation()

    """
    Get IP address Class.
    Its return one of these classes [A,B,C,D,E].
    Default Class is Unknown.
    """

    def get_class(self) -> str:
        if 0 <= self.octets[0] <= 127:
            self.ip_class = 'A'
        elif 128 <= self.octets[0] <= 191:
            self.ip_class = 'B'
        elif 192 <= self.octets[0] <= 223:
            self.ip_class = 'C'
        elif 224 <= self.octets[0] <= 239:
            self.ip_class = 'D'
        else:
            self.ip_class = 'E'
        return self.ip_class

    """
    Get IP address designation.
    Its return one of these designations [Public, Private, Special].
    Default Designation is Unknown.
    """

    def get_designation(self) -> str:
        octets = self.octets
        if octets[0] == 127:
            self.ip_designation = 'Special'
        elif octets[0] == 10 and 0 <= octets[1] <= 255:
            self.ip_designation = 'Private'
        elif octets[0] == 172 and 16 <= octets[1] <= 31:
            self.ip_designation = 'Private'
        elif octets[0] == 192 and octets[1] == 168:
            self.ip_designation = 'Private'
        else:
            self.ip_designation = 'Public'
        return self.ip_designation

    """
    Check if the IP is valid based on IPv4 regex pattern.
    """

    def check_validation(self):
        valid_ip = re.match(
            r"^((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$",
            self.ip)
        if not valid_ip:
            print("Opps, Invalid IP address!")
        else:
            self.is_valid_id = True

    """
    represent the output with nice formatting. 
    """

    def get_final_result(self):
        if self.is_valid_id:
            print(
                f'The IP address ({self.ip}) has class ({self.get_class()}) and designation ({self.get_designation()})')


if __name__ == '__main__':
    ipCalculator = IPCalculator(ip=sys.argv[1])
    ipCalculator.get_final_result()
