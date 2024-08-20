import sys
import os
import subprocess
import re
import time

file_cmd= '/content/cmd/cmdfile.txt'

cmd=[sys.executable, '/content/tensorflow/training.py']

while True:
    f = open(file_cmd, "r")
    line=f.readline()
    if line.find("START")>-1 :
        f.close()        
        print("FIND CMD START")
        f = open(file_cmd, "w")
        f.writelines("EXECUTED")
        f.close()
        with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
            for line in proc.stdout:
                 print(line)
            stdout, stderr = proc.communicate()
        result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)
    else:
        f.close()
    time.sleep(1)
