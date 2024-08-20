import sys
import os
import subprocess
import re
from parameter import *

setConfigFile()

#subprocess.run([sys.executable, '/content/tensorflow/generate_tf_records.py','-l',labelmap_path,'-o', train_record_path,'-i', dataset_images,'-csv',train_labels])

f = open(logfile_training, "w")

cmd=[sys.executable, '/content/tensorflow/generate_tf_records.py','-l',labelmap_path,'-o', train_record_path,'-i', dataset_images,'-csv',train_labels]
with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stderr:
         print(line,flush=True)
         f.write(line)
         f.flush()
    stdout, stderr = proc.communicate()
result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)


#subprocess.run([sys.executable, '/content/tensorflow/generate_tf_records.py','-l',labelmap_path,'-o', test_record_path,'-i', dataset_images,'-csv',test_labels])
cmd=[sys.executable, '/content/tensorflow/generate_tf_records.py','-l',labelmap_path,'-o', test_record_path,'-i', dataset_images,'-csv',test_labels]
with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stderr:
         print(line,flush=True)
         f.write(line)
         f.flush()
    stdout, stderr = proc.communicate()
result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)


#With the parameters set, start the training: 
print("<---------------START TRAINING--------->")
#subprocess.run([sys.executable, '/content/models/research/object_detection/model_main_tf2.py','--pipeline_config_path',pipeline_config_path,'--model_dir',model_dir,'--alsologtostderr','--num_train_steps',str(num_steps),'--sample_1_of_n_eval_examples',str(1),'--num_eval_steps',str(num_eval_steps)])
cmd=[sys.executable, '/content/models/research/object_detection/model_main_tf2.py','--pipeline_config_path',pipeline_config_path,'--model_dir',model_dir,'--alsologtostderr','--num_train_steps',str(num_steps),'--sample_1_of_n_eval_examples',str(1),'--num_eval_steps',str(num_eval_steps)]

print("CMD: ",cmd)

with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stderr:
         print(line,flush=True)
         f.write(line)
         f.flush()
    stdout, stderr = proc.communicate()
result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)
f.close()



