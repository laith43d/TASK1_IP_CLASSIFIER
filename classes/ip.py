class IP:
    def __init__(self,ip) -> None:
        self.value = ip
        self.without_mask = ip[0 : ip.index('/')]
        self.octets = list(map(int, self.without_mask.split(".")))
        self.ip_class, self.ip_designation = self.__get_class_and_designation()
    
    value: str
    without_mask: str
    octets: list
    ip_class: str
    ip_designation : str

    def __get_class_and_designation(self):
        if(self.octets[0] < 128):
            if(self.octets[0] == 10):
                return 'A','private'
            if(self.octets[0] == 127):
                return 'C','special'
            return 'A','public'

        if(self.octets[0] < 192):
            if(self.octets[0] == 172 and 32 > self.octets[1] > 15 ):
                return 'B','private'
            return 'B','public'

        if(self.octets[0] < 224):
            if(self.octets[0] == 192 and self.octets[1] == 168 ):
                return 'C','private'
            return 'C','public'

        if(self.octets[0] < 240):
            return 'D','special'

        return 'E','special'







