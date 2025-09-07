a=int(input())
count=0
while a/10!=0:
    count+=1
    a=a//10
print(f'Digit Count is:{count}')