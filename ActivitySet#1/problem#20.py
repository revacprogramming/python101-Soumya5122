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
<<<<<<< HEAD
        print("I love you")
=======
        print("I love me")
>>>>>>> 6e5e632b3600d24cf3e8c44cf1486d2757b02d04
    