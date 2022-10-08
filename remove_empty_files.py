import os

def remove_empty_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(dirpath, dirnames, filenames)
        if not dirnames and not filenames:
            os.rmdir(dirpath)

"""
example of the current directory
"""
remove_empty_files('.')
