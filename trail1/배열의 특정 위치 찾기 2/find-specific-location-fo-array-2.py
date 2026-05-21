arr=list(map(int,input().split()))
odd_arr=arr[::2]
even_arr=arr[1::2]

print(abs(sum(odd_arr)-sum(even_arr)))