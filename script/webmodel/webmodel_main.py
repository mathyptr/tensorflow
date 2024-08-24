#! /usr/bin/env python
import sys
import os
import subprocess
import re
import time

file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/webmodel/'

cmddownload=[sys.executable, script_dir+'download_dir.py']
print("CMD: ",cmddownload)
while True:
    try:
        f = open(file_cmd, "r")
        line=f.readline()
        if line.find("START")>-1 :
            f.close()        
            print("FIND CMD START")
            print("START DOWNLOAD MODEL")
            f = open(file_cmd, "w")
            f.writelines("START DOWNLOAD MODEL")
            f.close()

            with subprocess.Popen(cmddownload, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stderr:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(cmddownload, proc.returncode, stdout, stderr)

            print("DOWNLOAD MODEL EXECUTED")
            f = open(file_cmd, "w")
            f.writelines("DOWNLOAD MODEL EXECUTED")
            f.close()

        else:
            f.close()
    except FileNotFoundError:
        print('File CMD  does not exist')

    time.sleep(5)
