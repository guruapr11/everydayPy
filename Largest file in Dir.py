import os
size=0
max_size=0
root_dir='C:/Users/gururaj.naik/archive/'
for folder,sub_fol,files in os.walk(root_dir):
    for file in files:
        size=os.stat(os.path.join(folder,file)).st_size

        if size>max_size:
            max_size=size
            max_file=os.path.join(folder,file)

print("the largest file is:", max_file +" and is of: " +str(max_size)+" bytes")
