def solution():
    isErrorInOct = False
    IsNotValidIp = True

    ipClass = ""
    Designation = ""

    # make loop Until Write Valid Ip Address
    while IsNotValidIp:
        ipAddress = input('Please Enter Valid Ip Address like 127.0.0.1/24: ')
        octalForIp = ipAddress.split('.')

        if len(octalForIp) != 4:
            print('Ip Address Must Be Contain 4 Octal')
            continue

        lastOctWithSubnet = octalForIp[3].split('/')  # eg : x.x.x.1/24 => ["1", "24"]

        if len(lastOctWithSubnet) != 2 or lastOctWithSubnet[1] == "":
            print('Please Enter With Ip Address Correct Subnet Mask ')
            continue

        if lastOctWithSubnet[1] == "":
            print('Please Enter With Ip Address Correct Subnet Mask ')
            continue

        if not lastOctWithSubnet[1].isdigit():
            print('Subnet Mask Must Be Number ! ')
            continue

        if int(lastOctWithSubnet[1]) < 0 or int(lastOctWithSubnet[1]) > 32:
            print('Subnet Mask Must Be From 0 to 32')
            continue

        octalForIp[3] = lastOctWithSubnet[0]  # now to get just 4 octal without Subnet

        for octal in octalForIp:
            if octal.strip() == "":
                print('octal Must Be Not Empty')
                isErrorInOct = True
                break
            if not octal.isdigit():
                print('Ip Address Must Be Number !')
                isErrorInOct = True
                break
            if int(octal) < 0 or int(octal) > 255:
                print('Octal Must Be In Range from 0 To 255')
                isErrorInOct = True
                break

        # check If Octal Is Not Number And Not In Correct Range Then Return To Enter Avalid Ip
        if isErrorInOct:
            continue

        if 0 <= int(octalForIp[0]) <= 127:
            ipClass = "A"
            if int(octalForIp[0]) == 10:
                Designation = "Private"
            elif int(octalForIp[0]) == 127 and (0 <= int(octalForIp[1]) <= 255) and (
                    0 <= int(octalForIp[2]) <= 255) and (1 <= int(octalForIp[3]) <= 255):
                Designation = "Special"
            else:
                Designation = "Public"
        elif 128 <= int(octalForIp[0]) <= 191:
            ipClass = "B"
            if int(octalForIp[0]) == 172 and 16 <= int(octalForIp[1]) <= 31:
                Designation = "Private"
            else:
                Designation = "Public"

        elif 192 <= int(octalForIp[0]) <= 223:
            ipClass = "C"
            if int(octalForIp[0]) == 192 and int(octalForIp[1]) == 168:
                Designation = "Private"
            else:
                Designation = "Public"

        elif 224 <= int(octalForIp[0]) <= 239:
            ipClass = "D"
            Designation = "Multicasting"

        else:
            ipClass = "E"
            Designation = "Reserved"

        print("Output: Class: " + ipClass + ", Designation: " + Designation)

        writeAnotherIp = input('If You Want To Write Another Ip Address Write y Or Enter Any Letter To Close The '
                               'Program : ')

        if writeAnotherIp.upper() != 'Y':
            print('Good Bye')
            IsNotValidIp = False


if __name__ == '__main__':
    solution()
