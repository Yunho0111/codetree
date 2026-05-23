n=int(input())
arr=[]
arr.append(n)
i=1
ct=0
if n%5 == 0:
    ct+=1
    
for elem in arr:
    i+=1
    arr.append(n*i)
    if (n*i)%5 == 0:
        ct+=1
        if ct==2:
            break


for elem in arr:
    print(elem, end=' ')