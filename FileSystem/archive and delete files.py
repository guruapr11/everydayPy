# importing the required modules
import os
import time
import zipfile
import shutil

# main function
def main():

    # initializing the count
    archived_files_count = 0    

    # specify the path
    path = "C:/Users/gururaj.naik/logs"

    # specify the days
    days = 30

    # converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)

    # checking whether the file is present in path or not
    if os.path.exists(path):


        # iterating over each and every folder and file in the path
            for root_folder,folder,files in os.walk(path):
                            # checking the current directory files
                         
                for file in files:
                    file_path = os.path.join(root_folder, file)
                    if seconds >= get_file_or_folder_age(file_path):
                        move_files(file_path)
                        #archive_files(file_path)
                        archived_files_count += 1 # incrementing count
                        

    archive_files()
    remove_old_files()
    print(f"Total files archived: {archived_files_count}")    

    
def move_files(file_path):
    dest_folder_archive = "C:/Users/gururaj.naik/archive/"
    shutil.move(file_path, dest_folder_archive)

 
def archive_files():
    dest_folder_archive = "C:/Users/gururaj.naik/archive/"
    files = os.listdir(dest_folder_archive)
    for f in files:
        if f.endswith(".sql" or ".txt"):
            dfile_path=dest_folder_archive+f
            with zipfile.ZipFile(dfile_path + ".zip","w",zipfile.ZIP_DEFLATED) as zipObj:
                zipObj.write(dfile_path)
                
def remove_old_files():
    dest_folder_archive = "C:/Users/gururaj.naik/archive/"
    files_removed=0
    files = os.listdir(dest_folder_archive)
    for f in files:
        if not f.endswith(".zip"):
            f = dest_folder_archive+f
            os.remove(f)
            files_removed+=1
    print(f"Total files removed: {files_removed}") 

def get_file_or_folder_age(path):

    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.stat(path).st_mtime

    # returning the time
    return ctime


if __name__ == '__main__':
    main()