#function to determine the class of an Ip address
def findClass(ip_network):
  if(ip_network[0] >= 0 and ip_network[0] <= 127):
    return "A"
   
  elif(ip_network[0] >=128 and ip_network[0] <= 191):
    return "B"
   
  elif(ip_network[0] >= 192 and ip_network[0] <= 223):
    return "C"
   
  elif(ip_network[0] >= 224 and ip_network[0] <= 239):
    return "D"
   
  else:
    return "E"



def find_type_of_IP(ip_network):
  if (ip_network[0] >= 0 and ip_network[0] <= 8):
    return"Public"

  elif (ip_network[0] == 10):
    return"Private"
   
  elif(ip_network[0] == 172 and ip_network[1] >= 16 and ip_network[1] <= 31):
    return"Private"
   
  elif(ip_network[0] == 192 and ip_network[1] == 168):
    return"Private"

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