import os
import shutil

# A: blender / IR
# B: silhouette


img_dir = './full/Real/mask'

save_dir = './silnet_data/B'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for i, img in enumerate(os.listdir(img_dir)):
    shutil.copy('%s/%s' % (img_dir, img),
                '%s/silnet_B_%04d.png' % (save_dir, i+1001))