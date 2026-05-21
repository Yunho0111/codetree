arr=list(map(int,input().split()))
temp=[]
ct=0

for elem in arr:
    if elem != 0:
        temp.append(elem)
        ct=ct+1
    else:
        break

print(sum(temp), round(sum(temp)/ct,1))