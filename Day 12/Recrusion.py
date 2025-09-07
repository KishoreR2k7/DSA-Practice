def print_n_times(a):
    if a==0:
        return 0
    print(a)
    a-=1
    return print_n_times(a)
a=int(input())
print_n_times(a)