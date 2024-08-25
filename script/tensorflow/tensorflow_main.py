import sys
import os
import subprocess
import re
import time

file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/tensorflow/'

download_cmd=[sys.executable, script_dir+'download_dir.py']
op1_cmd=[sys.executable, script_dir + 'training.py']
op2_cmd=[sys.executable, script_dir + 'validate.py']
op3_cmd=[sys.executable, script_dir + 'export.py']
nextphase_cmd=[sys.executable, script_dir+'sendstartcmd.py']

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


            print("TRAINING")
            f = open(file_cmd, "w")
            f.writelines("TRAINING")
            f.close()

            with subprocess.Popen(op1_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(op1_cmd, proc.returncode, stdout, stderr)

            print("TRAINING EXECUTED")
            print("VALIDATION")
            f = open(file_cmd, "w")
            f.writelines("TRAINING EXECUTED")
            f.writelines("VALIDATION")
            f.close()

            with subprocess.Popen(op2_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(op2_cmd, proc.returncode, stdout, stderr)

            print("VALIDATION EXECUTED")
            print("EXPORT")
            f = open(file_cmd, "w")
            f.writelines("VALIDATION EXECUTED")
            f.writelines("EXPORT")
            f.close()

            with subprocess.Popen(op3_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(op3_cmd, proc.returncode, stdout, stderr)

            print("EXPORT EXECUTED")
            f = open(file_cmd, "w")
            f.writelines("EXPORT EXECUTED")
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

    time.sleep(1)
