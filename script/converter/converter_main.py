#! /usr/bin/env python
import sys
import os
import subprocess
import re
import time

file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/converter/'

cmddownload=[sys.executable, script_dir+'download_dir.py']
converter_cmd=[sys.executable, script_dir+'converter.py']
webmodel_cmd=[sys.executable, script_dir+'sendstartcmd.py']

print("CMD: ",converter_cmd)
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


            print("SEND WEBMODEL CMD")
            f = open(file_cmd, "w")
            f.writelines("SEND WEBMODEL CMD")
            f.close()

            with subprocess.Popen(webmodel_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(webmodel_cmd, proc.returncode, stdout, stderr)

            print("SEND WEBMODEL CMD EXECUTED")
            f = open(file_cmd, "w")
            f.writelines("SEND WEBMODEL CMD EXECUTED")
            f.close()



        else:
            f.close()
    except FileNotFoundError:
        print('File CMD  does not exist')

    time.sleep(5)
