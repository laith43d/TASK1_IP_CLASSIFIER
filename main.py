#murtada hayder

import re

def solution(value):
    #A
    if (value>str(0) and value<str(128)):
        if (re.match(r"^10\.", value)):
            return "Output: Class: A, Designation: Private"

        elif (re.match(r"^127\.1/\.|^127\.", value)):
            return "Output: Class: A, Designation: Special"

        else:
            return "Output: Class: A, Designation: Public"
                
    #B
    elif (value>str(127) and value<str(192)):
        if (re.match(r"(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)", value)):
            return "Output: Class: B, Designation: Private"
        elif (re.match(r"^169\.254\.", value)):
            return "Output: Class: B, Designation: Private"

        else:
            return "Output: Class: B, Designation: Public"
    #C
    elif (value>str(191) and value<str(224)):
        if (re.match(r"^192\.168\.", value)):
            return "Output: Class: C, Designation: Private"

        else:
            return "Output: Class: C, Designation: Public"
                
    #D
    elif (value>str(223) and value<str(240)):
        return "Output: Class: D, Designation: Public"

    #E
    elif (value>str(239) and value<str(256)):
        return "Output: Class: E, Designation: Public"

    else:
        return "Enter a valid IP"




if __name__ == '__main__':
    
    print(solution("127.0.0.1/24"))
    print(solution("192.168.1.1/24"))

