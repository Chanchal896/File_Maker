import os
import random
import string

def create():
    i=0
    while(i!=8):
            a=random.choices(string.ascii_letters,k=random.randint(1,10))
            f=open(F"{"".join(a)}.png",'w')
            i=i+1
    f.close()

    

s=os.chdir("Clutter folder")
create()
dircon=os.listdir(s)
print(dircon)
print(dircon)

x=0
i=0
for i in range(len(dircon)):
      if(dircon[i].endswith(".png")):
            a=dircon[i].split(".")[0]
            if(not a.isdigit()):
                x=x+1
                t=f"{x}.png"
                while t in dircon:
                  x=x+1
                  t=f"{x}.png"
                os.rename(dircon[i],t)    
            elif (a.isdigit()):
                  continue
      else:
            pass