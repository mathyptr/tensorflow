import sys
import os
import subprocess
import re


from config import *
from tokenJWT import *
from util import *

download_cmd=[sys.executable, script_dir+'download_dir.py']
op1_cmd=['rm','-r',tmp_dir]
op2_cmd=['rm','-r',work_dir]
op3_cmd=['mv',download_dir,home_dir]
src_csv=dataset_images+'/*.csv'
mvsrc_csv=dataset_images+'/*.csv'+work_dir
op4_cmd=['cp',dataset_images+'/'+file_train_labels,train_labels]
#op4_cmd=['mv',mvsrc_csv]

exec_cmd(op1_cmd) 

write_status("DOWNLOAD DATA")
exec_cmd(download_cmd) 
write_status("DOWNLOAD DATA EXECUTED")

write_status("CLEAN WORKING DIR")
exec_cmd(op2_cmd) 
exec_cmd(op3_cmd) 
exec_cmd(op4_cmd) 
print(op4_cmd)
write_status("CLEAN WORKING DIR")

