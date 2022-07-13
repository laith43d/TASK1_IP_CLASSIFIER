x = input("enter the IP address please:")


check = x.split('.')
check = [int(i) for i in check]

#Class A
if check[0] in range(128):
    print("clas: A")
    if check[0] in range(1, 10) or check[0] in range(11, 127):
        print("public")
    
    elif check[0]  == 10:
        print("private")
    else:
        print("special")    

#Class B    
elif check[0] in range(128, 192):
    print("class: B")
    if check[0] == 172 and check[1] in range(16, 32):
        print("private")
        
    elif check[0] == 172 and check[1] == 31:
        print("private")
    
    elif check[0] in range(128, 172) or check[0] in range(173, 192):
        print("public")
   
    else:
        print("special")  
    
    
#Class C  
elif check[0] in range(192, 224) :
    print("class: C")   
    
    if check[0] == 192 and check[1] == 168: 
        print("private")
    elif check[0] in range(192, 196):
        print("public")
    elif check[0] in range(197, 224):
        print("public")
    
    else:
        print("special")  

#Class D
elif check[0] in range(224, 240) :
    print("class: D") 
    print("special")  
    

#Class E
elif check[0] in range(240, 256):
    print("class: E")
    print("special")