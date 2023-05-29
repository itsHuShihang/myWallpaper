# -*- coding: UTF-8 -*-
import os

dirs = []
files = []

def traversal_files(path):
    for item in os.scandir(path):
        if item.is_dir():
            dirs.append(item.path)
        elif item.is_file():
            files.append(item.path)

    print('dirs:', dirs)
    print('files:', files)

def edit_readme_file(file_set):
    with open("README.md","w") as md:
        md.write("## This is the preview:\n")
        for file in file_set:
            md.write(file[2::])
            md.write(":\n")
            md.write("![pic](myWallpaper\\")
            md.write(file[2::])
            md.write(")\n")




if __name__ == '__main__':
    path1 = '.\\Japan'
    path2 = '.\\pic'
    traversal_files(path1)
    traversal_files(path2)
    edit_readme_file(files)