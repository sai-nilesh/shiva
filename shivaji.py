#CALCULATOR
a=float(input("ENTER A NUMBER:"))
b=float(input("ENTER A NUMBER2:"))
choice=input("ENTER A CHOICE:")
res=0
if(choice=="+"):
    res=a+b
    print(res)
elif(choice=="-"):
    res=a-b
    print(res)
elif(choice=="*"):
    res=a*b
    print(res)
elif(choice=="**"):
    res=a**b
    print(res)
elif(choice=="%"):
    res=a%b
    print(res)
elif(choice=="/"):
    res=a/b
    print(res)
else:
    print("UNKNOWN")
    





