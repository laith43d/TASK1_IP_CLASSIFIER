def solution():
    ip = input('Enter your IP: ')  # split and convert the ip into
    ip = ip.split('/')
    ipAdd = ip[0].split('.')
    first = (int(ipAdd[0]))
    second = (int(ipAdd[1]))
    third = (int(ipAdd[2]))
    fourth = (int(ipAdd[3]))

    if first in range(0, 128):  # ip class type
        print('The Class Type Is A')
    elif first in range(127, 192):
        print('The Class Type Is B')
    elif first in range(191, 224):
        print('The Class Type Is C')
    elif first in range(223, 240):
        print('The Class Type Is D')
    elif first in range(239, 256):
        print('The Class Type Is E')

    if first == 10 or first == 172 and second > 15 and second < 30 or first == 192 and second == 168:  # private or public or special
        print('The Designation Is : Private')

    elif first == 127 and fourth > 0:
        print('The Designation Is : Special')

    else:
        print('The Designation Is : Public')


if __name__ == '__main__':
    solution()
