arr=list(map(int,input().split()))
temp=[]
ct=0
sum=0
for elem in arr:
    if elem != 0:
        if elem%2 == 0:
            ct=ct+1
            sum=sum+elem
        continue
    else:
        break
print(ct,sum)
