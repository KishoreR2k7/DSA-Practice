a=int(input())
c=0
for i in range(2,a+1):
    if a%i==0 and i!=a:
        c=1
if c==0:
    print('It is Prime')
else:
    print('It is not Prime')