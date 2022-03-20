import helpers
from classes.ip import IP

def solution():
    value = input('Please give an IP address (IP/MASK): ') 

    try:
        ip = IP(value)
    except:
        return print(helpers.error_message)
    

    if(helpers.is_valid_ip(ip) == False):
        return print(helpers.error_message)


    print(helpers.get_info(ip))


if __name__ == '__main__':
    solution()
