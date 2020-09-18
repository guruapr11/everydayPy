import os
tcount=''
tcnt2=''
os.chdir("C:/Users/gururaj.naik/archive/")
with open ("new1.txt","r") as inp:
    tcount=inp.read()
with open ("new2.txt","r") as inp2:
    tcnt2=inp2.read()
tcount+=tcount+'\n'
tcnt2=tcount+tcnt2
with open ("new3.txt","w") as wr:
    wr.write(tcnt2)