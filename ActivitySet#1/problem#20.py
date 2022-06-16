count=0
n1=0
n2=1
while True:
    n=input('enter a number:')
    if n <= count:
        n=n1+n2
        n2=n1
        n1=n
        print(n1)
        continue
    