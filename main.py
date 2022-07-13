def findClass(ip):
    if 0 <= int(ip[0]) <= 127:
        return "A"

    elif 128 <= int(ip[0]) <= 191:
        return "B"

    elif 192 <= int(ip[0]) <= 223:
        return "C"

    elif 224 <= int(ip[0]) <= 239:
        return "D"
    else:
        return "E"


def findDesignation(pr):
    if 0 <= int(pr[0]) <= 127:
        if int(pr[0]) == 10:
            return "Private"
        elif int(pr[0]) == 127 and (0 <= int(pr[1]) <= 255) and (
                0 <= int(pr[2]) <= 255) and (1 <= int(pr[3]) <= 255):
            return "Special"
        else:
            return "Public"
    elif 128 <= int(pr[0]) <= 191:
        if int(pr[0]) == 172 and 16 <= int(pr[1]) <= 31:
            return "Private"
        else:
            return "Public"

    elif 192 <= int(pr[0]) <= 223:
        if int(pr[0]) == 192 and int(pr[1]) == 168:
            return "Private"
        else:
            return "Public"

    elif 224 <= int(pr[0]) <= 239:
        return "Public"

    else:
        return "Public"


def solution():
    import socket

    repeat = "Y"
    ipNotCorrect = True
    while repeat == "Y" or repeat == "y":
        hostname = socket.gethostname()
        ipAddress = socket.gethostbyname(hostname)
        # ipAddress = input("Enter ip  for testing if conditions")
        ip_split = ipAddress.split(".")
        print("\n\nYour Computer Name is: " + hostname)
        print("\nYour Computer IP Address is:" + ipAddress, "\nSo.. \n")
        # check the ip is correct or not
        if len(ip_split) != 4:
            print(f" ip {ip_split} is incorrect ip ☹️ \n\n")
            ipNotCorrect = False
        if (0 <= int(ip_split[0]) >= 255) or (0 <= int(ip_split[1]) >= 255) or (0 <= int(ip_split[2]) >= 255) or (
                0 <= int(ip_split[3]) >= 255):
            ipNotCorrect = False
            print(f" ip {ipAddress} is incorrect ip ☹️ because ip is out of range \n\n")
        if ipNotCorrect:
            print(f"The ip : {ipAddress} , is in Class: ", findClass(ipAddress), ", Designation: ", findDesignation(ipAddress))
        repeat = input(
            "If you want to Check ip again Write (Y) \n \t if you want to stop, type Something else 🙂 :\n ")


if __name__ == '__main__':
    solution()
