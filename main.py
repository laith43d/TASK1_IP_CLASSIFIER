import helpers


def solution():
    ipAddress = input('enter your ip address\n')
    # print(end='\n')
    spliting = ipAddress.split('/')
    # THIS WOULD GIVE US A SET OF IP AND SUBNET MASK
    splitedIp = spliting[0]
    # sybnet_
    pureIp = splitedIp.split('.')
    # classChecker =
    # print(pureIp)

    helpers.check_class(pureIp)


if __name__ == '__main__':
    solution()
# print('hello world')
