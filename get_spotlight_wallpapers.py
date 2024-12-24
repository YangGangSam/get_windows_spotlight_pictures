# Script Name   :   get Windows 10 spotlight pictures
# Author        :   yanggang
# Created       :   2018/6/11
        
import os
import shutil
import imghdr
import hashlib
from PIL import Image
import logging

def check_save_folder():
    global save_folder, save_folder_phone
    base_path = os.path.dirname(os.path.realpath(__file__))
    save_folder = os.path.join(base_path, 'wallpapers')
    save_folder_phone = os.path.join(base_path, 'wallpapers_phone')

    for folder in [save_folder, save_folder_phone]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            logging.info(f'Created folder: {folder}')
        else:
            # logging.info(f'Folder already exists: {folder}')
            continue

def process_wallpapers():
    no_new_wallpaper = True
    wallpapers = os.listdir(spotlight_wallpaper_folder)
    for wallpaper in wallpapers:
        wallpaper_path = os.path.join(spotlight_wallpaper_folder, wallpaper)
        if imghdr.what(wallpaper_path) == 'jpeg':
            with Image.open(wallpaper_path) as img:
                imgSize = img.size
                save_wallpaper_folder = save_folder if imgSize == (1920, 1080) else save_folder_phone if imgSize == (1080, 1920) else None
                if save_wallpaper_folder is None:
                    continue
            md5_hash = hashlib.md5(open(wallpaper_path, 'rb').read()).hexdigest()
            wallpaper_name = f"{md5_hash}.jpg"
            save_path = os.path.join(save_wallpaper_folder, wallpaper_name)
            if not os.path.exists(save_path):
                shutil.copyfile(wallpaper_path, save_path)
                logging.info(f'Saved {wallpaper_name} in {os.path.basename(save_wallpaper_folder)}.')
                no_new_wallpaper = False
    if no_new_wallpaper:
        logging.info(f'No new wallpapers found')

def main():
    logging.basicConfig(level=logging.INFO)
    check_save_folder()
    global spotlight_wallpaper_folder
    spotlight_wallpaper_folder = os.path.join(os.getenv('LOCALAPPDATA'), 'Packages', 'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy', 'LocalState', 'Assets')
    process_wallpapers()

if __name__ == '__main__':
    main()
