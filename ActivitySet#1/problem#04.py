# Conditional Execution
h=float(input("Enter hours: "))
r=float(input("Enter rate:"))
if h<=40:
  print("Pay:",(h*r))
else:
  print("Pay:",((40*r)+((h-40)*1.5*r)))
