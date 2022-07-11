ip= input(" enter a valid ip :")
ip_split=ip.split('.')
# print(ip_split)

if int(ip_split[0])>=1 and int(ip_split[0])<=127:
    print("class A")
    if int(ip_split[0])==10:
        print("private")
    else:
        print("public")
elif int(ip_split[0])>=128 and int(ip_split[0])<=191:
    print("class B")
    if int(ip_split[0])==172:
        print("private")
    else:
        print("public")
elif int(ip_split[0])>=192 and int(ip_split[0])<=223:
    print("class C")
    if int(ip_split[0])==192:
        print("private")
    else:
        print("public")
elif int(ip_split[0])>=224 and int(ip_split[0])<=239:
    print("class D")
elif int(ip_split[0])>=240 and int(ip_split[0])<=255:
    print("class E")


