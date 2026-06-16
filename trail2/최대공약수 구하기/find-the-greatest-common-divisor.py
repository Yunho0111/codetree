n, m = map(int, input().split())

# Please write your code here.
def gcd(x,y):
    if x%y==0:
        return y
    elif y==0:
        return x
    else:
        return gcd(y, x%y)
print(gcd(n,m))