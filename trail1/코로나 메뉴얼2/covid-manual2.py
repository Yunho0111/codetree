arr=[input().split() for _ in range(3)]
clinic=[0 for _ in range(4)]

for patient in arr:
    if patient[0]=='Y' and int(patient[1])>=37:
        clinic[0]+=1
    elif patient[0]=='N' and int(patient[1])>=37:
        clinic[1]+=1
    elif patient[0]=='Y' and int(patient[1])<37:
        clinic[2]+=1
    else:
        clinic[3]+=1


for elem in clinic:
    print(elem, end=' ')
if  clinic[0]>=2:
    print('E')