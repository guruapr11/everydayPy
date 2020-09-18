# importing the required modules
import os
import time

# main function
def main():

    # initializing the count
    deleted_files_count = 0

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
        for root_folder,files in os.walk(path):
                            # checking the current directory files
            for file in files:

                    # file path
                file_path = os.path.join(root_folder, file)

                    # comparing the days
                if seconds >= get_file_or_folder_age(file_path):

                        # invoking the remove_file function
                    remove_file(file_path)
                    deleted_files_count += 1 # incrementing count


    print(f"Total files deleted: {deleted_files_count}")



def remove_file(path):

    # removing the file
    if not os.remove(path):

        # success message
        print(f"{path} is removed successfully")

    else:

        # failure message
        print(f"Unable to delete the {path}")


def get_file_or_folder_age(path):

    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.stat(path).st_mtime

    # returning the time
    return ctime


if __name__ == '__main__':
    main()