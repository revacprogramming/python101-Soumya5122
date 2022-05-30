# Loops & Iterators

largest = None
smallest = None

while True:
    n = input("Enter a number? ")
    if n == "done":
        break

    try :
        num=int(n)
    except:
        print("Invalid input")
        continue
    if largest==None:
        largest=n
    if largest>None:
        largest=n
    if smallest==None:
        smallest=n
    if smallest>None:
        smallest=n

print("Maximum is", largest)
print("Minimum is",smallest)

