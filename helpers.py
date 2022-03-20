from classes.ip import IP


error_message = '''
    Invalid IP !!!
    
    - Please give a valid IP address in "n.n.n.n/mask" format. 
    - each "n" must range from 0 to 255.
    - "mask" must range from 0 to 32.
    - for example:  
      127.22.232.23/24
'''

def is_valid_ip(ip : IP) -> bool:

    # must containt four octets
    if(len(ip.octets) != 4):
        return False
    
    # octets must range from 0 to 255
    for octet in ip.octets:
        if(octet < 0 or octet > 255):
            return False

    

    # --------------- mask validation ----------------
    mask:str
    try:
        mask = int(ip.value[ip.value.index('/') + 1:])
        
        # must range from 0 to 32
        if(mask < 0 or mask > 32):
            return False

    except:
        return False



def get_info(ip:IP):
    return f'''
    Class: {ip.ip_class}, Designation: {ip.ip_designation}
    
    finish
    '''