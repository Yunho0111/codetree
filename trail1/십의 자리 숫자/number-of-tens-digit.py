arr=list(map(int,input().split()))
cnt_arr=[0]*10

for elem in arr:
    if elem==0:
        break
    if elem >=10:
        ten=int(elem/10)
        cnt_arr[ten]+=1

for i in range(1,10):
    cnt=cnt_arr[i]
    print(f"{i} - {cnt}")

    
