class Myclass:
        print("\" WELCOME TO MY PROGRAM \"")
        print("I CAN found\n\"class of ip\"\n type of ip \"specific or public\"")
        def ip_mathed(self):
            input_ip = input("Enter the your option please :")
            classs_A = range(0, 128)
            classs_B = range(128, 192)
            classs_c = range(192, 224)
            class_D = range(224, 240)
            classs_E = range(240, 256)
            reang_CB = range(16, 32)
            z= input_ip.split(".")
            if  int(z[0]) in classs_A :
                print(f"This {input_ip} found in class \"A\"")
                if int(z[0]) == 127  :
                        print(f"This{input_ip} is \"special\"")
                elif int(z[0])  == 10 :
                        print(f"This {input_ip} is \'private\' ")
                else:
                        print(f"This {input_ip} is \'public\'  ")
            if int(z[0]) in classs_B :
                print(f"This {input_ip} found in class \"B\"")
                if int(z[0]) == 172 and int(z[1]) in reang_CB:
                    print(f"This {input_ip} is  \'private\' ")
                else:
                    print(f"This {input_ip} is  \'public\' ")
            elif int(z[0]) in classs_c :
                print(f"This {input_ip} found in class \"C\"")
                if int(z[0]) == 192 and int(z[1]) == 168:
                    print(f"This {input_ip} is  \'private\' ")
                else:
                    print(f"This {input_ip} is  \'public\' ")
            elif int(z[0]) in class_D :
                print(f"This {input_ip} found in class \"D\"")
                print(f"This{input_ip} is \"special\"")
            elif int(z[0]) in classs_E :
                print(f"This {input_ip} found in class \"E\"")
                print(f"This{input_ip} is \"special\"")
obj=Myclass()
obj.ip_mathed()