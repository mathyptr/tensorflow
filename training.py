import sys
import os
import subprocess
import re
from parameter import *

setConfigFile()

subprocess.run([sys.executable, '/content/tensorflow/generate_tf_records.py','-l',labelmap_path,'-o', train_record_path,'-i', dataset_images,'-csv',train_labels])
subprocess.run([sys.executable, '/content/tensorflow/generate_tf_records.py','-l',labelmap_path,'-o', test_record_path,'-i', dataset_images,'-csv',test_labels])

#With the parameters set, start the training: 
subprocess.run([sys.executable, '/content/models/research/object_detection/model_main_tf2.py','--pipeline_config_path',pipeline_config_path,'--model_dir',model_dir,'--alsologtostderr','--num_train_steps',str(num_steps),'--sample_1_of_n_eval_examples',str(1),'--num_eval_steps',str(num_eval_steps)])

