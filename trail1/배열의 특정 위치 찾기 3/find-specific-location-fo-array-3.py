arr=list(map(int,input().split()))
temp=[]

for elem in arr:
    temp.append(elem)
    if elem == 0:
        break
n=len(temp)
sum_arr=temp[n-4:n-1]
print(sum(sum_arr))