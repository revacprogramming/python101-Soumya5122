
# Functions


def computepay(h, r):
<<<<<<< HEAD
    if h<=40:
        pay=(h*r)
    else:
        pay=(40*r)+((h-40)*1.5*r)
    return pay 
   #you can also return variable name
   # (which r defined) return value stores in place of
   #  none if any value is not returned then the output
   #   will be none.
=======
  if h<=40:
    pay=(h*r)
  else:
    pay=(40*r)+((h-40)*1.5*r)
  return pay
>>>>>>> e4187dd5339fc93afe8ac6bd398090d807787873

h = float(input("Enter hours? "))
r = float(input("Enter rate per hour? "))

<<<<<<< HEAD
p = computepay(h, r)
print("Pay", p)
=======

h = float(input("Enter hours? "))
r = float(input("Enter rate per hour? "))

p = computepay(h, r)
print("Pay", p)
>>>>>>> e4187dd5339fc93afe8ac6bd398090d807787873
