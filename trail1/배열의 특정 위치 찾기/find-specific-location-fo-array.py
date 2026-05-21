arr=list(map(int,input().split()))

even_arr=arr[1::2]
mul3_arr=arr[2::3]
print(sum(even_arr),round(sum(mul3_arr)/len(mul3_arr),1))