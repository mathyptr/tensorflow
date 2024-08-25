import sys
import os
import subprocess
import re
from config_augmentation import *

#Image Augmentation
print("<---------------START AUGMENTATION--------->")

f = open(logfile_augmentation, "w")

cmd=[sys.executable, '/content/augmentation/augment_annotated_boxes.py',image_coco_json,imageout_dir,'-n',str(num_iterations),'-s']

with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stderr:
         print(line,flush=True)
         f.write(line)
         f.flush()
    stdout, stderr = proc.communicate()
result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)
f.close()
