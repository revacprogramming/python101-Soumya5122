<<<<<<< HEAD
# Files

filename = open("dataset/mbox-short.txt", "r")
print(filename.readline())
=======
fh = open('romeo.txt','r')
l = list()
for line in fh:
    line = line.split()
    for word in line:
        if word not in l:
            l.append(word)
print(sorted(l))
>>>>>>> e4187dd5339fc93afe8ac6bd398090d807787873
