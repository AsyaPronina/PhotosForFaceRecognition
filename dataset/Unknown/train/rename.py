import os
import re

for r, d, f in os.walk(r'C:\Study\DL\repository\PhotosForFaceRecognition\dataset\Unknown\train'):
        for file in f:
            if '.jpg' in file:
                new_name = re.sub('indoor|outdoor', 'unknown', file)
                os.rename(os.path.join(r, file), os.path.join(r, new_name))       