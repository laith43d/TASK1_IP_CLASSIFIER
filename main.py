#function to determine the class of an Ip address

from re import I


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
  
  #public and private ip of class A
  if (ip_network[0] == 10 ):
    return"Private"

  elif (
    ip_network[0] >= 1 and ip_network[0] <= 127 
  and ip_network[1] == 0  
  and ip_network[2] == 0 
  and ip_network[3] == 0 
      ):
    return"Public"

  #public and private ip of class B
  elif (ip_network[0] == 172 and ip_network[1] >= 16 and ip_network[1] <= 31 ):
    return"Private"

  elif(ip_network[0] >= 128 and ip_network[0] <= 191 ):
    return"Public"
  
   
  #public and private ip of class C
  elif (ip_network[0] == 192 and ip_network[1] == 168 ):
    return"Private"

  elif (
    ip_network[0] >= 192 and ip_network[0] <= 223 
  and ip_network[1] >= 0 and ip_network[1] <= 255 
  and ip_network[2] >= 0 and ip_network[2] <= 255 
      ):
    return"Public"


  #Public ip of class D
  elif (ip_network[0] >= 224 and ip_network[0] <= 239 ):
    return"Public"

  #Public ip of class E
  elif (
    ip_network[0] >= 240 and ip_network[0] <= 255 
      ):
    return"Public"
  
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


  while True:
    #Asking if the user want to restart the program 
    #Or Exit the Program
    again = input("Do you want to Exit this program.  n/y   ")
    if again not in {"y","n"}:
        print("Enter y to exit or n to continue.")               
    elif again == "n":
        #Keep Restarting the Program
        ip = input('Enter the ip Address = ')
        ip = ip.split('/')
        ip_network = ip[0].split('.')
        ip_mask = ip[1]
        ip_network = [int(i) for i in ip_network]
        print(print("class :", networkClass))
        print("Designation :", ipch)
    elif again == "y":
        # Exit the Program
        print("Exiting the Program.......see you later :) ")
        break