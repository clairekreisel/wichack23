import random

f=open("testval.csv", 'w')
f.write("merge,bills\n")
for i in range(51):
    j=0
    f.write(f"{i},{j}\n")
f.close()
