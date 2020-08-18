import sys
import os
import glob
import numpy as np
from PIL import Image


dir_path = None

try:
    dir_path = sys.argv[1]
except IndexError:
    print('Base directory path is required.')
    sys.exit(1)

glob_path = os.path.join(dir_path, '*')

for i, file_path in enumerate(glob.glob(glob_path), 1):
    img = Image.open(file_path)
    img_np = np.array(img)
    print(i, os.path.basename(file_path), img_np.shape)

