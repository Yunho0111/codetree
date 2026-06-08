n = int(input())

# Please write your code here.
def pr_numsq(num):
    for i in range(num):
        for j in range(num):
            print((num*i+j)%9+1, end=' ')
        print()
        
            
pr_numsq(n)