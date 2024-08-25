#! /usr/bin/env python
import sys
import os
import subprocess
import re
import time

file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/webmodel/'

download_cmd=[sys.executable, script_dir+'download_dir.py']
print("CMD: ",download_cmd)
while True:
    try:
        f = open(file_cmd, "r")
        line=f.readline()
        if line.find("START")>-1 :
            f.close()        
            print("FIND CMD START")

            print("START DOWNLOAD DATA")
            f = open(file_cmd, "w")
            f.writelines("START DOWNLOAD DATA")
            f.close()

            with subprocess.Popen(download_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stderr:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(download_cmd, proc.returncode, stdout, stderr)

            print("DOWNLOAD DATA EXECUTED")
            f = open(file_cmd, "w")
            f.writelines("DOWNLOAD DATA EXECUTED")
            f.close()


        else:
            f.close()
    except FileNotFoundError:
        print('File CMD  does not exist')

    time.sleep(5)
