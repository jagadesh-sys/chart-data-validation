import glob
import shutil
import os

src_dir = r"C:\Users\JagadeshP-Kairos\Downloads\Training_dataset_02\BarGraph"
dst_dir = r"C:\Users\JagadeshP-Kairos\Downloads\New folder"

for jpgfile in glob.iglob(os.path.join(src_dir, "*.png")):
    for i in range(10):
        shutil.copy2(jpgfile, dst_dir)
