import random

import cv2
import os
import glob
import numpy as np
from PIL import Image

from get_dataset import get_dataset
from update_image_and_anno import update_image_and_anno

OUTPUT_SIZE = (600, 600)  # Height, Width
SCALE_RANGE = (0.3, 0.7)
FILTER_TINY_SCALE = 1 / 50  # if height or width lower than this scale, drop it.

ANNO_DIR = '/path/to/annotation/directory'
IMG_DIR = '/path/to/image/directory'

# Names of all the classes as they appear in the Pascal VOC Dataset
category_name = ['aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow','diningtable','dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor']


# Change the output path of the imwrite commands to wherever you want to get both the mosaic image and the image with boxes
def main():
    img_paths, annos = get_dataset(ANNO_DIR, IMG_DIR)

    idxs = random.sample(range(len(annos)), 4)

    new_image, new_annos = update_image_and_anno(img_paths, annos,
                                                 idxs,
                                                 OUTPUT_SIZE, SCALE_RANGE,
                                                 filter_scale=FILTER_TINY_SCALE)

    cv2.imwrite('output.jpg', new_image) #The mosaic image
    for anno in new_annos:
        start_point = (int(anno[1] * OUTPUT_SIZE[1]), int(anno[2] * OUTPUT_SIZE[0]))
        end_point = (int(anno[3] * OUTPUT_SIZE[1]), int(anno[4] * OUTPUT_SIZE[0]))
        cv2.rectangle(new_image, start_point, end_point, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.imwrite('output_box.jpg', new_image) # The mosaic image with the bounding boxes
    
    yolo_anno = []
    
    for anno in up_annos:
      tmp = []
      tmp.append(anno[0])
      tmp.append((anno[3]+anno[1])/2)
      tmp.append((anno[4]+anno[2])/2)
      tmp.append(anno[3]-anno[1])
      tmp.append(anno[4]-anno[2])
      yolo_anno.append(tmp)

    with open('output.txt', 'w') as file: # The output annotation file will appear in the output.txt file
      for line in yolo_anno:
        file.write((' ').join([str(x) for x in line]) + '\n')   

if __name__ == '__main__':
    main()
