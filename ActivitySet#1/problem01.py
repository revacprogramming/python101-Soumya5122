

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
f.close()
