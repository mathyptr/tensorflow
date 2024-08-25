#! /usr/bin/env python
import sys
import os
import subprocess
import re
import time

file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/converter/'

download_cmd=[sys.executable, script_dir+'download_dir.py']
op1_cmd=[sys.executable, script_dir+'converter.py']
nextphase_cmd=[sys.executable, script_dir+'sendstartcmd.py']

print("CMD: ",op1_cmd)
while True:
    try:
        f = open(file_cmd, "r")
        line=f.readline()
        if line.find("START")>-1 :
            f.close()        
            print("FIND CMD START")

            print("DOWNLOAD DATA")
            f = open(file_cmd, "w")
            f.writelines("DOWNLOAD DATA")
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




            print("CONVERTER")
            f = open(file_cmd, "w")
            f.writelines("CONVERTER")
            f.close()

            with subprocess.Popen(op1_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(op1_cmd, proc.returncode, stdout, stderr)

            print("CONVERTER EXECUTED")
            f = open(file_cmd, "w")
            f.writelines("CONVERTER EXECUTED")
            f.close()


            print("SEND CMD NEXT PHASE")
            f = open(file_cmd, "w")
            f.writelines("SEND CMD NEXT PHASE")
            f.close()

            with subprocess.Popen(nextphase_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(nextphase_cmd, proc.returncode, stdout, stderr)

            print("SEND CMD NEXT PHASE EXECUTED")
            f = open(file_cmd, "w")
            f.writelines("SEND CMD NEXT PHASE EXECUTED")
            f.close()




        else:
            f.close()
    except FileNotFoundError:
        print('File CMD  does not exist')

    time.sleep(5)
