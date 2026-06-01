n,q=map(int,input().split())
arr=list(map(int,input().split()))

for _ in range(q):
    ques=list(map(int,input().split()))
    if ques[0] == 1:
        a=ques[1]-1
        print(arr[a])
    elif ques[0] == 2:
        b=ques[1]
        if b in arr:
            result = arr.index(b) + 1
            print(result)
        else:
            print(0)
    else:
        s=ques[1]-1
        e=ques[2]
        temp=arr[s:e]
        print(*temp)
