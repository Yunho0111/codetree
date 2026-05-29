a,b=map(int,input().split())
div=[0]*b
result=0

while a>1:
    rem=a%b
    div[rem]+=1
    a=a//b

for elem in div:
    result+=elem**2

print(result)