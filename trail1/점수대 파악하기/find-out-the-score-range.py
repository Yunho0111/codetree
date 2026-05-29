arr=list(map(int,input().split()))
cnt_arr=[0 for _ in range(11)]

for elem in arr:
    if elem>9:
        ten=int(elem/10)
        cnt_arr[ten]+=1
    elif elem==0:
        break
    else:
        continue


for i in range(10,0,-1):
    cnt=cnt_arr[i]
    print(f"{i}0 - {cnt}")
    