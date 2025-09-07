a=int(input())
b=a
c=0
while a/10!=0:
    c=c*10+(a%10)
    a=a//10
if b==c:
    print('It is a Palindrom')
else:
    print('It is not Palindrom')