#murtada hayder
#If you don't like my code you should check your eyes.(JK)
#regex 

import re

def solution(ip):

    value = ip.split(".")
    first_value = int(value[0])
    #A
    if (first_value > 0 and first_value < 128):
        if (re.match(r"^10\.", ip)):
            return "Output: Class: A, Designation: Private"

        elif (re.match(r"^127\.1/\.|^127\.", ip)):
            return "Output: Class: A, Designation: Special"

        else:
            return "Output: Class: A, Designation: Public"
                
    #B
    elif (first_value > 127 and first_value < 192):
        if (re.match(r"(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)", ip)):
            return "Output: Class: B, Designation: Private"
        elif (re.match(r"^169\.254\.", ip)):
            return "Output: Class: B, Designation: Private"

        else:
            return "Output: Class: B, Designation: Public"
    #C
    elif (first_value > 191 and first_value < 224):
        if (re.match(r"^192\.168\.", ip)):
            return "Output: Class: C, Designation: Private"

        else:
            return "Output: Class: C, Designation: Public"
                
    #D
    elif (first_value> 223 and first_value < 240):
        return "Output: Class: D, Designation: Public"

    #E
    elif (first_value > 239 and first_value < 256):
        return "Output: Class: E, Designation: Public"

    else:
        return "Enter a valid IP"




if __name__ == '__main__':
    
    print(solution("127.0.0.1/24"))
    print(solution("192.168.1.1/24"))
