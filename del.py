import os

import re

def rename_files():

 file_list = os.listdir(r"./")

 saved_path = os.getcwd()

 print("current working directory is"+ saved_path)

 os.chdir(r"./")

 for file_name in file_list:

  new_name = "".join(filter(lambda ch: ch not in '-', file_name))#引号中的文字为需要去掉的字符

  os.rename(file_name , new_name)

 os.chdir(saved_path)

rename_files()
