
def solution():
    pass
#IP input
IP = str(input('Enter IP:'))

#Making the String to list
IPtoList = list(IP.split('.'))

#Converting String to int
IP_inx_1 = (int(IPtoList[0]))
IP_inx_2 = (int(IPtoList[1]))
IP_inx_3 = (int(IPtoList[2]))
IP_inx_4 = (int(IPtoList[3]))

print(IPtoList)
print(IP_inx_1)
print(IP_inx_2)
print(IP_inx_3)
print(IP_inx_4)

if IP_inx_1 in range(1,128) and IP_inx_2 == 0 and IP_inx_3 == 0 and IP_inx_4 == 0:
    print('IP class is A and Public')

elif IP_inx_1 == 10 and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
    print('IP is class A and Private')

elif IP_inx_1 in range(128,192) and IP_inx_2 in range(0,256) and IP_inx_3 == 0 and IP_inx_4 == 0:
    print('IP class is B and Public')

elif IP_inx_1 == 127 and IP_inx_2 in range(16,32) and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
    print('IP class is B and Privet')

elif IP_inx_1 in range(192,224) and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 == 0:
    print('IP class is C and Public')

elif IP_inx_1 == 192 and IP_inx_2 in 168 and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
    print('IP class is C and Privet')

elif IP_inx_1 in range(224,240) and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
    print('IP class is D')

elif IP_inx_1 in range(240,256) and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 in range(0,256):
    print('IP class is E')

elif IP_inx_1 == 127 and IP_inx_2 in range(0,256) and IP_inx_3 in range(0,256) and IP_inx_4 in range(1,256):
    print('This is a Special IP')
else:
    print('You entered a wroing IP')



if __name__ == '__main__':
    pass

solution()