import os
import shutil
from directories import get_file_formats


def organize(path):
    directory = os.listdir(path)
    file_formats = get_file_formats()
    
    for file in directory:
        filename, extension = os.path.splitext(file)
        
        if extension in file_formats:
            src_dir = f"{path}/{file}"
            target_dir = f"{path}/{file_formats[extension]}"
            
            if os.path.exists(target_dir):
                shutil.move(src_dir, target_dir)
            else:
                os.makedirs(target_dir)
                shutil.move(src_dir, target_dir)
