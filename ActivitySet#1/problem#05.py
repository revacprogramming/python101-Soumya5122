Score =input("Enter score:")
s=float(Score)
if s>0 and s<1:
    if s>=0.6:
        print("A")
    elif s>=0.9:
        print("N")
    elif s<=0.3:
        print("S")
else:
    print("Oops there is an ERROR.")