import os
import shutil

img_dir = './hof'

save_dir = './aligned'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


for i, file in enumerate(os.listdir(img_dir)):
    shutil.move('%s/%s' % (img_dir, file),
                '%s/%04d.png' % (save_dir, i+2728))