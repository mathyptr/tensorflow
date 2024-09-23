#! /usr/bin/env python
import sys
import os
import subprocess
import re
import time
from config import *
from  jwtlib.api_jwt import PyJWT
from datetime import datetime, timedelta
from tokenJWT import *

file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/converter/'

download_cmd=[sys.executable, script_dir+'download_dir.py']
op1_cmd=['rm','-r',download_dir]
op2_cmd=['rm','-r',work_dir]
op3_cmd=['mv',download_dir,home_dir]
op4_cmd=[sys.executable, script_dir+'converter.py']
nextphase_cmd=[sys.executable, script_dir+'sendstartcmd.py']

def exec_cmd(cmd):
    with subprocess.Popen(op1_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
        for line in proc.stdout:
            print(line)
        stdout, stderr = proc.communicate()
    result = subprocess.CompletedProcess(op1_cmd, proc.returncode, stdout, stderr)


exec_cmd(op1_cmd) 
print(op1_cmd)
exec_cmd(op2_cmd)
print(op2_cmd)
exec_cmd(op3_cmd)
print(op3_cmd)

while True:
    try:
        f = open(file_cmd, "r")
        line=f.readline()
        if line.find("START")>-1 :
            f.close()        
            print("FIND CMD START")


            print("CLEAN")
            f = open(file_cmd, "w")
            f.writelines("CLEAN")
            f.close()

            exec_cmd(op1_cmd) 

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

            try:
             
              
                print("CONVERTER")
                f = open(file_cmd, "w")
                f.writelines("CONVERTER")
                f.close()


                checkToken()

                with subprocess.Popen(op4_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                    for line in proc.stdout:
                     print(line)
                    stdout, stderr = proc.communicate()
                result = subprocess.CompletedProcess(op2_cmd, proc.returncode, stdout, stderr)

                print("CONVERTER EXECUTED")
                f = open(file_cmd, "w")
                f.writelines("CONVERTER EXECUTED")
                f.close()

                createToken()

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
            except:
                print('Wrong token')

        else:
            f.close()
    except FileNotFoundError:
        print('File CMD  does not exist')

    time.sleep(5)
