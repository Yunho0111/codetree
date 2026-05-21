arr=list(map(int,input().split()))
temp=[]
for elem in arr:
    temp.append(elem)
    if elem%3==0:
        break

n=len(temp)
print(temp[n-2])