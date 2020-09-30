print("Enter 1 or 0")
n=int(input())
if n==0 or n==1:

    if bool(n)==True :
        for i in range(1,6):
            for j in range(1,i+1):
                print("*",end=" ")
            print("\r")

    elif bool(n)==False :
        for i in range(1,6):
            for j in range(i,6):
                print("*",end=" ")
            print("\r")
else :
    print("Error in input")