def solution():
    ip = str(input('Enter the IP address:'))
    parts = ip.split('/')[0].split('.')
    p1, p2, p4 = int(parts[0]), int(parts[1]), int(parts[3])

    if p1 == 10 or p1 == 169 and p2 == 254 or p1 == 172 and p2 in range(16, 32) or p1 == 192 and p2 == 168:
        designation = 'Private'
    elif p1 == 127 and p4 != 0: designation = 'Special'
    else: designation = 'Public'
    
    Class = ''
    if   p1 in range(0  , 128):
        Class = 'A'
    elif p1 in range(128, 192):
        Class = 'B'
    elif p1 in range(192, 224):
        Class = 'C'
    elif p1 in range(224, 240):
        Class = 'D'
    else:
        Class = 'E'
    
    print(f'Class: {Class}, Designation: {designation}')
    
if __name__ == '__main__':
    solution()
    