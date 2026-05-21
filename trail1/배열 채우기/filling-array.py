arr=list(map(int,input().split()))
temp=[]

for elem in arr:
    if elem != 0:
        temp.append(elem)
    else:
        break

rev_temp=temp[::-1]

for elem in rev_temp:
    print(elem,end=' ')