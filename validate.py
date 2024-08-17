import sys
import os
import subprocess
import re
from parameter import *

setConfigFile();
#Validate the model
subprocess.run([sys.executable, '/content/models/research/object_detection/model_main_tf2.py','--pipeline_config_path',pipeline_config_path,'--model_dir',model_dir,'--checkpoint_dir',model_dir])


