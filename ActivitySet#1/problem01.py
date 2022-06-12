

f=open("randomrona.txt","r")
print(f.read())
print("\n\n")
f.close()

f=open("randomrona.txt","a")
f.write("Nahi main chutiya nahi\n mai ")
f.close()

f=open("randomrona.txt","r")
print(f.read())
print("\n\n")

import os
if os.path.exists("randomrona.txt"):
    os.remove("randomrona.txt")
else:
    print("the file doenot exists")
f.close()
