# Script Name   :   get Windows 10 spotlight pictures
# Author        :   yanggang
# Created       :   2018/6/11
        
import os
import shutil
import imghdr
from PIL import Image
import hashlib


def savefolder():
    # save folder
    global save_folder_temp, save_folder, save_folder_phone
    save_folder_temp = os.path.dirname(os.path.realpath(__file__)) + '\\wallpapers_temp'
    save_folder = os.path.dirname(os.path.realpath(__file__)) + '\\wallpapers'
    save_folder_phone = os.path.dirname(os.path.realpath(__file__)) + '\\wallpapers_phone'
    
    if os.path.exists(save_folder_temp):
        print('existed')
    else:
        os.makedirs(save_folder_temp)

    if os.path.exists(save_folder):
        print('existed')
    else:
        os.makedirs(save_folder)

    if os.path.exists(save_folder_phone):
            print('existed')
    else:
        os.makedirs(save_folder_phone)


def wallpapers_temp():
    wallpapers = os.listdir(wallpaper_folder)
    for wallpaper in wallpapers:
        wallpaper_path = os.path.join(wallpaper_folder, wallpaper)
        if imghdr.what(wallpaper_path) == 'jpeg':
            # 计算文件的 MD5 哈希值
            md5_hash = hashlib.md5()
            with open(wallpaper_path, 'rb') as f:
                while chunk := f.read(8192):
                    md5_hash.update(chunk)
            wallpaper_name = md5_hash.hexdigest() + '.jpg'
            save_path = os.path.join(save_folder_temp, wallpaper_name)
            shutil.copyfile(wallpaper_path, save_path)
            # print('save wallpaper ' + save_path)


def wallpapers_filter():
    wallpapers_2 = os.listdir(save_folder_temp)
    for wallpaper_2 in wallpapers_2:
        wallpaper_2_path = os.path.join(save_folder_temp, wallpaper_2)
        img = Image.open(wallpaper_2_path)
        imgSize = img.size
        # 筛选出 1920 * 1080 / 1080 * 1920分辨率的壁纸
        if (imgSize == (1920, 1080)):
            save_2_path = os.path.join(save_folder, wallpaper_2)
            shutil.copyfile(wallpaper_2_path, save_2_path)
            print('save desktop wallpaper ' + save_2_path)
        elif (imgSize == (1080, 1920)):
            save_3_path = os.path.join(save_folder_phone, wallpaper_2)
            shutil.copyfile(wallpaper_2_path, save_3_path)
            print('save phone wallpaper ' + save_3_path)
        else:
            continue


def main():

    savefolder()

    # wallpapers folder
    global wallpaper_folder
    wallpaper_folder = os.getenv('LOCALAPPDATA') + ('\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')

    #first filter
    wallpapers_temp()

    # second filter
    wallpapers_filter()

    # delete temp folder
    shutil.rmtree(save_folder_temp)
    input()

if __name__ == '__main__':
    main()

