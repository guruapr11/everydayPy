import os
from collections import Counter
os.chdir('C:/tech/python/')
#search_str="guru"
count=0
with open ('C:/tech/python/students.txt') as fread:
    c=Counter(fread.read().split())
    #for line in fread.readlines():
    #    if search_str in line:
    #        count+=1
    #print("String is found {0} times".format(count))
    print(c)