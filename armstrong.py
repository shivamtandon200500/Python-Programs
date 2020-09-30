def dig(num):
    s=0
    while(num!=0):
        a=num%10
        s=s+(a*a*a)
        num=num//10
    return s

def check(num):
    temp=num
    while num>0:
        if(temp==dig(num)):
            print("ss",dig(num))
            break
        else:
            num=num+1
check(320)