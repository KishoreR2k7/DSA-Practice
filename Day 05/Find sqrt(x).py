def sqrt(a):
    i=0
    while i*i<=a:
        i+=1
    return i-1
a=5
print(f'Square root in int:{sqrt(a)}')