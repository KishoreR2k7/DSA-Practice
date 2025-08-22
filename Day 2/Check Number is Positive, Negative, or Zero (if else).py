def checknumber(a):
    if a>0:
        print('It is Positive')
    elif a<0:
        print('It is Negative')
    else:
        print('It is zero')
        return 1
    
a=int(input())
checknumber(a)