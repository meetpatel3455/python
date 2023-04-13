def fibo(n):
    a,b=0,1

    while a<n:
        yield a
        a,b=b,b+1



x=fibo(16)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())