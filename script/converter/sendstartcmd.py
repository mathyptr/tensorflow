#!/usr/bin/env python3

import sys
import os
import subprocess
import re
from config_conv import *


#SEND START CMD
print("<---------------SEND START CMD---------->")

f = open(logfile_converter, "w")

cmd=['curl',startcmd]
print("CMD: ",cmd)
with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
    for line in proc.stderr:
         print(line,flush=True)
         f.write(line)
         f.flush()
    stdout, stderr = proc.communicate()
result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)
f.close()
