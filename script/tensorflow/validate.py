import sys
import os
import subprocess
import re
from parameter import *
import signal

setConfigFile();
#Validate the model
print("<---------------START VALIDATE--------->")
#subprocess.run([sys.executable, '/content/models/research/object_detection/model_main_tf2.py','--pipeline_config_path',pipeline_config_path,'--model_dir',model_dir,'--checkpoint_dir',model_dir])
cmd=[sys.executable, '/content/models/research/object_detection/model_main_tf2.py','--pipeline_config_path',pipeline_config_path,'--model_dir',model_dir,'--checkpoint_dir',model_dir]

print("CMD: ",cmd)

f = open(logfile_validate, "w")
checkpoint_founded=0
with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stderr:
         print(line,flush=True)
         f.write(line)
         f.flush()
         if line.find("INFO:tensorflow:Waiting for new checkpoint") >-1 :
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>Waiting for new checkpoint",flush=True)
#            if line.find("Found new checkpoint") == -1 :
            checkpoint_founded+=1
            if checkpoint_founded == 2 :
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>NOT Found new checkpoint",flush=True)
                proc.send_signal(signal.SIGINT)
    stdout, stderr = proc.communicate()
result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)
f.close()
