#! /usr/bin/env python
import sys
import os
import subprocess
import re
import time

file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/converter/'

converter_cmd=[sys.executable, script_dir+'converter.py']
print("CMD: ",converter_cmd)
while True:
    try:
        f = open(file_cmd, "r")
        line=f.readline()
        if line.find("START")>-1 :
            f.close()        
            print("FIND CMD START")
            print("START CONVERTER")
            f = open(file_cmd, "w")
            f.writelines("START CONVERTER")
            f.close()

            with subprocess.Popen(converter_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(converter_cmd, proc.returncode, stdout, stderr)

            print("CONVERTER EXECUTED")
            f = open(file_cmd, "w")
            f.writelines("CONVERTER EXECUTED")
            f.close()

        else:
            f.close()
    except FileNotFoundError:
        print('File CMD  does not exist')

    time.sleep(5)
