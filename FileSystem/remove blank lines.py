'''import os
import re
tcount=0
os.chdir("C:/Users/gururaj.naik/archive/")
with open ("new1.txt","r") as inp, open ("new12.txt","w") as f2 :
    for i in inp:
        if i.strip():
            f2.write(i)
    print(tcount)     '''   


import fileinput
import os
os.chdir("C:/Users/gururaj.naik/archive/")
for line in fileinput.FileInput("new1.txt",inplace=True):
    if line.rstrip():
         print(line,end ='')
'''extras'''
'''
import fileinput 
  
# Using fileinput.lineno() method 
for line in fileinput.input(files ='gfg.txt'): 
    print('{}. '.format(fileinput.lineno()) + line) 
'''