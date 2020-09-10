import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if len(sys.argv) < 3:
    print ("not enough")
else:
    print(sys.argv[0])

for i in range(len(sys.argv)):
    print (sys.argv[i])

