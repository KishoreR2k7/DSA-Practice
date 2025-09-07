def name_n_times(a):
    if a==0:
        return 0
    a-=1
    print('Name')
    return name_n_times(a)
a=int(input())
name_n_times(a)