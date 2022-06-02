# Loops & Iterators

largest = 0
smallest = 0

while True:
    n = input("Enter a number? ")
    if n == "done":
        break

    try :
        num=int(n)
    except:
        print("Invalid input")
        continue
        
    num=int(n)
    if largest is 0:
        largest=num
    if smallest is 0:
        smallest=num

    if largest<num:
        largest=num
    if smallest>num:
        smallest=num

print("Maximum is", largest)
print("Minimum is",smallest)

