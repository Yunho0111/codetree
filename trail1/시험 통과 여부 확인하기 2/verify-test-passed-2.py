n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
ct=0
for stu in range(n):
    if sum(arr[stu])/4 >= 60:
        print('pass')
        ct+=1
    else:
        print('fail')

print(ct)