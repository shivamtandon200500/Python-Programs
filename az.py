if __name__ == '__main__':
    n = int(input())
    arr= map(int, input().split())
    A=[]
    A.extend(arr)
    A.sort()
    length=len(A)
    if A[-2]==A[-1]:
        print(A[-3])
    else:
        print(A[-2])