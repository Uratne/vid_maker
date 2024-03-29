#!/usr/bin/env python
from cartoonizer import cartoonize
import cv2
import os
import time

in_dir = './imgs/input'
out_dir = './imgs'

arr = os.listdir(in_dir)
sorted_arr = sorted(arr)
for f in sorted_arr:
    image = cv2.imread(os.path.join(in_dir, f))
    print('==============')
    print(f)
    start_time = time.time()
    output = cartoonize(image)
    end_time = time.time()
    print("time: {0}s".format(end_time-start_time))
    name = os.path.basename(f)
    tmp = os.path.splitext(name)
    name = tmp[0] + tmp[1]
    name = os.path.join(out_dir, name)
    cv2.imwrite(name, output)
