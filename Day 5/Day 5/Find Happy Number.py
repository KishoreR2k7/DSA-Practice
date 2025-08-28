def is_happy(a):
    while a!=1 and a!=4:
        sum=0
        while a>0:
            sum+=(a % 10)**2
            a//=10
        a=sum
    return a==1
a=19
print(is_happy(a))
