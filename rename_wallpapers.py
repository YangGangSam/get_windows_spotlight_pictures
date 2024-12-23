import os
import hashlib
import shutil
import imghdr

def rename_wallpapers(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if imghdr.what(file_path) in ['jpeg', 'png', 'jpg']:
                md5_hash = hashlib.md5()
                with open(file_path, 'rb') as f:
                    while chunk := f.read(8192):
                        md5_hash.update(chunk)
                new_name = md5_hash.hexdigest() + os.path.splitext(file)[1]
                new_file_path = os.path.join(root, new_name)
                shutil.move(file_path, new_file_path)
                print(f'Renamed: {file_path} to {new_file_path}')

def main():
    wallpapers_folder = 'wallpapers'
    wallpapers_phone_folder = 'wallpapers_phone'
    
    rename_wallpapers(wallpapers_folder)
    rename_wallpapers(wallpapers_phone_folder)

if __name__ == '__main__':
    main() 