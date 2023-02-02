import os
import sys
from pathlib import Path
import random
import shutil

dir = "C://Folder//to//root//"    # folder root
images_folder = dir + "images//"
annotations_folder = dir + "labels//"

'''
    Rename the image/annotation file
'''
image_list = os.listdir(images_folder)
for i in range(len(image_list)):
    # get image file
    image_file = image_list[i]

    # split filename & ext
    img_name, img_ext = os.path.splitext(image_file)

    # change image name to new serial number
    os.rename(images_folder + image_file, images_folder + str(i) + img_ext)

    # change annotation name to new serial number
    os.rename(annotations_folder + img_name + ".txt", annotations_folder + str(i) + ".txt")

'''
    shuffle
'''
output_dir = dir + "output//"
train_folder = output_dir + "train//"
valid_folder = output_dir + "valid//"
test_folder = output_dir + "test//"
train_percentage = 0.70
valid_percentage = 0.20
test_percentage = 0.10

# init folders
if os.path.exists(output_dir):
    if os.path.exists(dir + "output_backup//"):
        shutil.rmtree(dir + "output_backup//")
    shutil.copytree(output_dir, dir + "output_backup//")
    shutil.rmtree(output_dir)
for folders in [train_folder, valid_folder, test_folder]:
    os.makedirs(folders)
    os.makedirs(folders + "images//")
    os.makedirs(folders + "labels//")

# shuffle the order
image_list = os.listdir(images_folder)
random.shuffle(image_list)

def split_files(subfolder, index_begin, index_end):
    for i in range(index_begin, index_end):
        # get image file
        image_file = image_list[i]

        # split filename & ext
        img_name, img_ext = os.path.splitext(image_file)

        # move image to subfolder
        shutil.move(images_folder + image_file, subfolder + "images//" + image_file)

        # move annotation to subfolder
        shutil.move(annotations_folder + img_name + ".txt", subfolder + "labels//" + img_name + ".txt")

split_files(train_folder, 0, int(len(image_list)*train_percentage))
split_files(valid_folder, int(len(image_list)*train_percentage), int(len(image_list)*(train_percentage+valid_percentage)))
split_files(test_folder, int(len(image_list)*(train_percentage+valid_percentage)), len(image_list))
