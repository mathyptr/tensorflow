import sys
import os
import subprocess
import re
from parameter import *

setConfigFile()
#Export the model
subprocess.run([sys.executable, '/content/models/research/object_detection/exporter_main_v2.py','--trained_checkpoint_dir',model_dir,'--output_directory',output_directory,'--pipeline_config_path',pipeline_config_path])

