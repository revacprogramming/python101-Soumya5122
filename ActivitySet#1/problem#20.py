count=1
n1=0
n2=1
while True:
    N=input('enter a number:')
    n=int(N)

    if n <= count:
        n=n1+n2
        n2=n1
        n1=n
        print(n1)
        
        continue
    else:
        print("I love me")
    