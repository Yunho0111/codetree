n=int(input())
arr=[1,n]

for i in range(15):
    x=arr[i]+arr[i+1]
    arr.append(x)
    if x > 100:
        break

for elem in arr:
    print(elem,end=' ')