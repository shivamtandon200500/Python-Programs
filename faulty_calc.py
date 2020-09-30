print("enter 1 no.")
n1=int(input())
print("enter 2 no.")
n2=int(input())
print("enter operation")
o=input()
if o=="+" or o=="-" or o=="*" or o=="/":
    if o=="+":
        if (n1==56 and n2 ==9) or (n1==9 and n2 ==56):
            print(77)
        else:
            print(n1+n2)
    elif o=="-":
        print(n1-n2)
    elif o=="*":
        if (n1==45 and n2 ==3) or (n1==3 and n2 ==45):
            print(555)
        else:
            print(n1*n2)
    else :
        if (n1==56 and n2 ==6) or (n1==6 and n2 ==56):
            print(4)
        else:
            print(n1/n2)
else:
    print("wromg operand")