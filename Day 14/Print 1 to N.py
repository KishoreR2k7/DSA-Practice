def print_numbers(a):
    if a==0:
        return
    print_numbers(a-1)
    print(a)

a=int(input())
print_numbers(a)
