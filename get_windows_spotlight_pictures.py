# 获取 Windows 的锁屏壁纸

import os
import sys
import shutil
#import time
from PIL import Image

# 暂存目录 wallpapers_temp 及 最终存放目录 wallpapers
save_folder_temp = dir_path = os.path.dirname(os.path.realpath(__file__)) + '\wallpapers_temp'
save_folder = dir_path = os.path.dirname(os.path.realpath(__file__)) + '\wallpapers'

# 获取锁屏壁纸存储位置
wallpaper_folder = os.getenv('LOCALAPPDATA') + ('\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')

# 列出所有的文件
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

# 上面提取出的壁纸有些是不符合我们的要求的，所以下面进一步筛选

# 列出暂存目录下的所有文件
wallpapers_2 = os.listdir(save_folder_temp)

for wallpaper_2 in wallpapers_2:
    wallpaper_2_path = os.path.join(save_folder_temp, wallpaper_2)
    img = Image.open(wallpaper_2_path)
    imgSize = img.size
    # 筛选出 1920 * 1080 分辨率的壁纸
    if (imgSize != (1920, 1080)):
        continue
    save_2_path = os.path.join(save_folder, wallpaper_2)
    shutil.copyfile(wallpaper_2_path, save_2_path)
    print('save_2 wallpaper' + save_2_path)

# TODO
# 1. 删除暂存文件
# 2. 筛选步骤过于复杂
# 3. 存储位置的创建
