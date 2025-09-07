def print_numbers(a):
    if a==1:
        return 0
    a-=1
    print(a)
    return print_numbers(a)
a=int(input())
print_numbers(a)