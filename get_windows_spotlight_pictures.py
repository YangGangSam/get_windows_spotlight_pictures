# Script Name   :   get Windows 10 spotlight pictures
# Author        :   yanggang
# Created       :   2018/6/11
        
import os
import shutil
import sys
from PIL import Image


def savefolder():
    # save folder
    global save_folder_temp, save_folder
    save_folder_temp = os.path.dirname(os.path.realpath(__file__)) + '\\wallpapers_temp'
    save_folder = os.path.dirname(os.path.realpath(__file__)) + '\\wallpapers'
    
    if os.path.exists(save_folder_temp):
        print('existed')
    else:
        os.makedirs(save_folder_temp)

    if os.path.exists(save_folder):
        print('existed')
    else:
        os.makedirs(save_folder)


def first_filter():
    wallpapers = os.listdir(wallpaper_folder)
    for wallpaper in wallpapers:
        wallpaper_path = os.path.join(wallpaper_folder, wallpaper)
        # 先初步筛选，貌似也没啥用
        if (os.path.getsize(wallpaper_path) / 1024) < 150:
            continue
        time = os.path.getctime(wallpaper_path)
        wallpaper_name = str(time) + '.jpg'
        save_path = os.path.join(save_folder_temp, wallpaper_name)
        shutil.copyfile(wallpaper_path, save_path)
        print('save wallpaper' + save_path)


def second_filter():
    wallpapers_2 = os.listdir(save_folder_temp)
    for wallpaper_2 in wallpapers_2:
        wallpaper_2_path = os.path.join(save_folder_temp, wallpaper_2)
        img = Image.open(wallpaper_2_path)
        imgSize = img.size
        # 筛选出 1920 * 1080 / 1080 * 1920分辨率的壁纸
        if (imgSize != (1920, 1080)) and (imgSize !=(1080, 1920)):
            continue
        save_2_path = os.path.join(save_folder, wallpaper_2)
        shutil.copyfile(wallpaper_2_path, save_2_path)
        print('save_2 wallpaper' + save_2_path)


def main():

    savefolder()

    # wallpapers folder
    global wallpaper_folder
    wallpaper_folder = os.getenv('LOCALAPPDATA') + ('\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')

    #first filter
    first_filter()

    # second filter
    second_filter()

    # delete temp folder
    shutil.rmtree(save_folder_temp)

if __name__ == '__main__':
    main()
