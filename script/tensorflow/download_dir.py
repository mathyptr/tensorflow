#!/usr/bin/env python3

import sys
import os
import subprocess
import re
from config import *


#START DOWNLOAD
print("<---------------START DOWNLOAD--------->")

f = open(logfile_download, "w")

cmd=['wget','-r','-nH','-nc','-P',tmp_dir,'-o',logfile_wget,download_URL]
print("CMD: ",cmd)
with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stderr:
         print(line,flush=True)
         f.write(line)
         f.flush()
    stdout, stderr = proc.communicate()
result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)
f.close()
