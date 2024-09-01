import sys
import os
import subprocess
import re
from config import *


#Convert the model
print("<---------------START CONVERTER--------->")

f = open(logfile_converter, "w")

cmd=['tensorflowjs_converter','--input_format','tf_saved_model','--signature_name','serving_default','--saved_model_tags','serve '+inference_dir+' '+ model_dir]
print("CMD: ",cmd)
with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stderr:
         print(line,flush=True)
         f.write(line)
         f.flush()
    stdout, stderr = proc.communicate()
result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)
f.close()
