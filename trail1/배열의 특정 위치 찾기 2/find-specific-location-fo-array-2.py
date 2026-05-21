arr=list(map(int,input().split()))
odd_arr=arr[::2]
even_arr=arr[1::2]
sum_odd=sum(odd_arr)
sum_even=sum(even_arr)
print(abs(sum_odd-sum_even))