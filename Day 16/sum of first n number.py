def sum_first_n(n):
    if n == 0:
        return 0
    return n+sum_first_n(n-1)

a=int(input())
print(f'Sum of first {a} numbers is{sum_first_n(a)}')
