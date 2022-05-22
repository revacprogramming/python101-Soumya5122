# Conditional Execution

    hrs = float(input("Enter hours: "))
    rte = float(input("Enter rate:"))
    if hrs>=40:
      print("Pay:" hrs*rte)
      
    else:
    print("Pay:" (40*rte)+((hrs-40)*1.5*rte))
