import sys
import os
import subprocess
import re
from parameter import *

setConfigFile()
#Export the model
print("<---------------START EXPORT--------->")
#subprocess.run([sys.executable, '/content/models/research/object_detection/exporter_main_v2.py','--trained_checkpoint_dir',model_dir,'--output_directory',output_directory,'--pipeline_config_path',pipeline_config_path])

f = open(logfile_export, "w")

cmd=[sys.executable, '/content/models/research/object_detection/exporter_main_v2.py','--trained_checkpoint_dir',model_dir,'--output_directory',output_directory,'--pipeline_config_path',pipeline_config_path]
with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stderr:
         print(line,flush=True)
         f.write(line)
         f.flush()
    stdout, stderr = proc.communicate()
result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)
f.close()
