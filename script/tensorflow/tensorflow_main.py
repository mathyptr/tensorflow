import sys
import os
import subprocess
import re
import time

file_cmd= '/content/cmd/cmdfile.txt'
script_dir='/content/tensorflow/'
training_cmd=[sys.executable, script_dir + 'training.py']
validate_cmd=[sys.executable, script_dir + 'validate.py']
export_cmd=[sys.executable, script_dir + 'export.py']

while True:
    try:
        f = open(file_cmd, "r")
        line=f.readline()
        if line.find("START")>-1 :
            f.close()        
            print("FIND CMD START")
            print("START TRAINING")
            f = open(file_cmd, "w")
            f.writelines("START TRAINING")
            f.close()

            with subprocess.Popen(training_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(training_cmd, proc.returncode, stdout, stderr)

            print("TRAINING EXECUTED")
            print("START VALIDATION")
            f = open(file_cmd, "w")
            f.writelines("TRAINING EXECUTED")
            f.writelines("START VALIDATION")
            f.close()

            with subprocess.Popen(validate_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(validate_cmd, proc.returncode, stdout, stderr)

            print("VALIDATION EXECUTED")
            print("START EXPORT")
            f = open(file_cmd, "w")
            f.writelines("VALIDATION EXECUTED")
            f.writelines("START EXPORT")
            f.close()

            with subprocess.Popen(export_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
                for line in proc.stdout:
                 print(line)
                stdout, stderr = proc.communicate()
            result = subprocess.CompletedProcess(export_cmd, proc.returncode, stdout, stderr)

            print("EXPORT EXECUTED")
            f = open(file_cmd, "w")
            f.writelines("EXPORT EXECUTED")
            f.close()

        else:
            f.close()
    except FileNotFoundError:
        print('File CMD  does not exist')

    time.sleep(1)
