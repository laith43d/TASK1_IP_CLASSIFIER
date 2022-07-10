#function to determine the class of an Ip address
from ast import And


def findClass(ip_network):
  if(
    ip_network[0] >= 0 and ip_network[0] <= 127 
  and ip_network[1] >= 0 and ip_network[1] <= 255 
  and ip_network[2] >= 0 and ip_network[2] <= 255
  and ip_network[3] >= 0 and ip_network[3] <= 255
    ):
    return "A"
   
  elif(
    ip_network[0] >= 128 and ip_network[0] <= 191 
  and ip_network[1] >= 0 and ip_network[1] <= 255 
  and ip_network[2] >= 0 and ip_network[2] <= 255
  and ip_network[3] >= 0 and ip_network[3] <= 255
    ):
    return "B"
   
  elif(
    ip_network[0] >= 192 and ip_network[0] <= 223 
  and ip_network[1] >= 0 and ip_network[1] <= 255 
  and ip_network[2] >= 0 and ip_network[2] <= 255
  and ip_network[3] >= 0 and ip_network[3] <= 255
    ):
    return "C"
   
  elif(
    ip_network[0] >= 224 and ip_network[0] <= 239 
  and ip_network[1] >= 0 and ip_network[1] <= 255 
  and ip_network[2] >= 0 and ip_network[2] <= 255
  and ip_network[3] >= 0 and ip_network[3] <= 255
    ):
    return "D"
   
  else:
    return "E"



def find_type_of_IP(ip_network):
  
  #public ip of class A
  if (
    ip_network[0] >= 1 and ip_network[0] <= 127 
  and ip_network[1] == 0  
  and ip_network[2] == 0 
  and ip_network[3] == 0 
      ):
    return"Public"

  #public ip of class B
  elif(
    ip_network[0] >= 128 and ip_network[0] <= 191 
  and ip_network[1] >= 0 and ip_network[1] <= 255 
  and ip_network[2] == 0 
  and ip_network[3] == 0 
      ):
    return"Public"
   
  #public ip of class C
  elif (
    ip_network[0] >= 192 and ip_network[0] <= 223 
  and ip_network[1] >= 0 and ip_network[1] <= 255 
  and ip_network[2] >= 0 and ip_network[2] <= 255 
      ):
    return"Public"


  #Public ip of class D
  elif (
    ip_network[0] >= 224 and ip_network[0] <= 239 
      ):
    return"Public"

    #Public ip of class E
  elif (
    ip_network[0] >= 240 and ip_network[0] <= 255 
      ):
    return"Public"

#____________________________________________________________________________



  #private ip of class A
  elif (
    ip_network[0] == 10 
      ):
    return"Private"
   
  #private ip of class B
  elif (
    ip_network[0] == 172 and ip_network[1] >= 16 and ip_network[1] <= 31 
      ):
    return"Private"

  #private ip of class C
  elif (
    ip_network[0] == 192 and ip_network[1] == 168 
      ):
    return"Private"

  #private ip of class D
  elif (
    ip_network[0] >= 224 and ip_network[0] <= 239
      ):
    return"Private"

    #private ip of class E
  elif (
    ip_network[0] >= 240 and ip_network[0] <= 255
      ):
    return"Private"

#____________________________________________________________


#Special ip of class C
  elif (
    ip_network[0] == 127 and ip_network[3] >= 1 and ip_network[3] <= 255
      ):
    return"Special"

  else:
    return"Special"



#driver's code
if __name__ == "__main__":
   

  ip = input('Enter the ip Address = ')
  ip = ip.split('/')
  ip_network = ip[0].split('.')
  ip_mask = ip[1]


  ip_network = [int(i) for i in ip_network]
   

  #getting the network class
  networkClass = findClass(ip_network)
  print("class :", networkClass)


  #getting the IP address designation
  ipch = find_type_of_IP(ip_network)
  print("Designation :", ipch)