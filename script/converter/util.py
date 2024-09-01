#! /usr/bin/env python
import sys
import os
import subprocess
from config import *

def exec_cmd(cmd):
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
        for line in proc.stdout:
            print(line)
        stdout, stderr = proc.communicate()
    result = subprocess.CompletedProcess(cmd, proc.returncode, stdout, stderr)

def write_status(text):
    print(text)
    f = open(file_cmd, "w")
    f.writelines(text)
    f.close()
