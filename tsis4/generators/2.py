def gene(n):
    for i in range(n):  
        if i%2==0:
            yield i
        elif n%2==0 and i==n-1:
            yield ''
        else:
            yield ','


for i in gene(int(input())):
    print(i ,end='')