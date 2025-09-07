a=int(input())
b=a
len=len(str(a))
sum=0
while a/10!=0:
    sum+=(a%10)**len
    a=a//10
if b==sum:
    print('It is a Amstrong')
else:
    print('It is not a Amstrong')