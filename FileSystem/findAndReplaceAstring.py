import os
str_name="apple"
root_dir='C:/Users/gururaj.naik/archive/'
for folder,subfol,files in os.walk(root_dir):
    print("folder:",folder)
    if os.path.isdir('C:/Users/gururaj.naik/logs/'):
        for file in files:
            fname=os.path.join(folder,file)
            if os.path.isfile(fname):
                with open(fname, 'r') as file :
                    filedata = file.read()
                    filedata = filedata.replace("apple", "chocs")
                    print(filedata)
                with open(fname, 'w') as file :    
                    file.write(filedata)