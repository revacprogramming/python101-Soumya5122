count=0
total=0
file=open("romeo.txt",'r')

for line in file:
    count=count+1
    x=line.find(':')
    n=line[x+1:].strip()
    value=float(n)
    total=total+value
    average=total/count
    break
print("Average:",average)
print(file)