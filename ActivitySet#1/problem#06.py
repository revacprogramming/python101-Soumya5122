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
        largest=num
    elif largest>None:
        largest=num
    if smallest==num:
        smallest=num
    elif smallest>num:
        smallest=num

print("Maximum is", largest)
print("Minimum is",smallest)

