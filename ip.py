def checkIP(testIp):
        """
        This method Check given IP
        """    
        workingIP = [0, 0, 0, 0]
        ipmask = testIp.split('/')
        splitIP = ipmask[0].split('.')
        if len(splitIP) != 4: raise ValueError

        for index in range(len(splitIP)):
            workingIP[index] = int(splitIP[index])
            if workingIP[index] > 255: raise ValueError
            if index > 3: raise ValueError
        return workingIP


def getClass(workingIP):
        """
        This method calculates the class of the given IP address.
        Returns a string 'A', 'B', 'C', 'D' or 'E'
        """

        ipClass = ''
        test = workingIP[0]
  
        if test >= 0 and test <= 127:
            ipClass = 'A'

        elif test > 127 and test <= 191:
            ipClass = 'B'

        elif test > 191 and test <= 223:
            ipClass =  'C'

        elif test > 223 and test <= 239:
            ipClass = 'D'

        elif test > 239 and test <= 255:
            ipClass = 'E'

        return ipClass



def getDesignation(workingIP):
        """
        This method Return the designation ipDesignation as a string
        """

        ipDesignation = ''
        ipClass = getClass(workingIP)
        
#class A
        if ipClass == 'A':
            if workingIP[0] == 10:
                ipDesignation = 'Private'

            elif workingIP[0] == 127 and workingIP[1] + workingIP[2] + workingIP[3] > 0:
                ipDesignation = 'Special'
            else:
                ipDesignation = 'Public'

#class B
        elif ipClass == 'B':
            if workingIP[0] == 169 and workingIP[1] == 254:
                ipDesignation = 'Private APIPA'
            if workingIP[0] == 172 and workingIP[1] >= 16 and workingIP[1] <= 31:
                ipDesignation = 'Private'            
            else:
                ipDesignation = 'Public'            

#class C
        elif ipClass == 'C':
            if workingIP[0] == 192 and workingIP[1] == 168:
                ipDesignation =  'Private'

            else:
                ipDesignation = 'Public'

#class D
        elif ipClass == 'D':
 
            ipDesignation = 'Special'

#class E
        elif ipClass == 'E':

            ipDesignation = 'Special'

        else:
            ipDesignation = 'Public'

        return ipDesignation

