f=open("romeo.txt","r")
fh=f.read()
lst=list()
for line in fh:
    line=line .split(":")
    for word in fh:
        if word not in lst:
            print(lst.append(word))
print(sorted(lst))