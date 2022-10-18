# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:01:53 2020

@author: shu
"""


import glob

path = 'data/'

def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        for jpg_file in glob.glob(image_path + '*png'):
            tf.write(jpg_file + '\n')

generate_train_and_val(path + 'train_images/', path + 'train.txt')
generate_train_and_val(path + 'val_images/', path + 'val.txt')