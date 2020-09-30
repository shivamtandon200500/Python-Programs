n=10
num=0
print("Enter a no.")
while(True):
    num=int(input())
    if num>10 :
        print("Try again")
        print("less than num")
        continue
    elif num <10:
        print("Try again")
        print("more than num")
    else:
        print("found",num)
        break