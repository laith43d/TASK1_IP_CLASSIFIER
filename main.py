def solution():
 while True :

    pass

#input
    IP = input("write your IP address : ip/mask ")

#split the ip address & mask
    ip= IP.split('/')


    ip_split = ip[0].split('.')

    octet1 = (int(ip_split[0]))
    octet2 = (int(ip_split[1]))



    elif (octet1) in range(192, 224):
#validation checks
    if len(ip_split) > 4 or len(ip_split) < 4 :
        print(" IP Address is :  invalid")
    elif octet1 > 255 or octet1 < 0:
        print(" IP Address is :  invalid")
    else:


        # class Types
     if (octet1) in range(0, 128):
      print("class Type = A")
     elif (octet1) in range(128, 192):
       print("class Type = B")
     elif (octet1) in range(192, 224):
        print("class Type = C")
     elif (octet1) in range(224, 240):
       print("class Type = D")
     elif (octet1) in range(240, 256):
       print("class Type = E")


#Designation Types

     if octet1 == 10:
          print(" IP Designation is : Private")
     elif octet1 == 172 and octet2 >= 16 and octet2 <= 31:
           print(" IP Designation is : Private ")
     elif octet1 == 192 and octet2 == 168:
          print(" IP Designation is : Private ")
     elif octet1 == 127 :
          print(" IP Designation is : Special ")


     else:
         print("IP Address is :  public ")

if __name__ == '__main__':
    pass

    solution()

