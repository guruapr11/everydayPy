import os
os.chdir('C:/tech/python')
fwr1= open('large1.txt','w')
fwr2= open('large2.txt','w')
with open('largeFile.txt') as myFile:

    for num, line in enumerate(myFile, 1):
        if num>10:
            fwr1.writelines(line)
            if num>20:
                fwr2.writelines(line)


