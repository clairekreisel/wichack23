import random

f=open("testval.txt", 'w')
f.write("merge,bills\n")
for i in range(51):
    j=random.randint(0,100)
    f.write(f"{i},{j}\n")
f.close()
