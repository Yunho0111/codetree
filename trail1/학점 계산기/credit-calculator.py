n=int(input())
arr=list(map(float,input().split()))

avg=round(sum(arr)/n,1)
print(avg)
if avg>=4:
    print('Perfect')
elif avg>=3 and avg<4:
    print('Good')
else:
    print('Poor')