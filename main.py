 def solution():
  
    ip=input("enter the ip ")

    #ip="192.168.1.1"
    ip_split=ip.split('.')
    ip_split[0] = int(ip_split[0])
    ip_split[1] = int(ip_split[1])
    ip_split[2] = int(ip_split[2])
    ip_split[3] = int(ip_split[3])
    if ip_split[0]==10:
        print("class: a ,designation: private ")
        
    elif ip_split[0] >=1 and ip_split[0]<=127:
        print('class a , designation public')
        
    elif ip_split[0]==127 :
        print('class a, designation special ')       

    elif ip_split[0]==172 and ip_split[1]==16 :
        print('class b , designation private')
        
        
        
    elif ip_split[0]>=28 and  ip_split[0]<=191:
        print('class b , designation public ')   
        


    elif ip_split[0]==192 and ip_split[1]==168:
        print('class c , designation private')
        
        
    elif ip_split[0]>=192 and ip_split[0]<=233:
        print('class c , designation public')    
        
        
        
    elif ip_split[0]>=224 and ip_split[0]<=239:
        print('class d , designation public')    
        
        
    elif ip_split[0]>=240 and ip_split[0]<=255:
        print('class e , designation public')    
        
        
        
    else:
        
        return 0 ;
        

if name == 'main':
      solution()
