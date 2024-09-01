#! /usr/bin/env python
import sys
import os
import subprocess
import re
from config import *
from tokenJWT import *
from util import *


download_cmd=[sys.executable, script_dir+'download_dir.py']
op1_cmd=['rm','-r',tmp_dir]
op2_cmd=['rm','-r',work_dir]
op3_cmd=['mv',download_dir,home_dir]

print("CMD: ",download_cmd)
while True:
    try:
        f = open(file_cmd, "r")
        line=f.readline()
        if line.find("START")>-1 :
            f.close()        
            print("FIND CMD START")

            write_status("CLEAN DOWNLOAD DIR")
            exec_cmd(op1_cmd)


            write_status("START DOWNLOAD DATA")
            exec_cmd(download_cmd) 
            write_status("DOWNLOAD DATA EXECUTED")


            try:
                checkToken()
                exec_cmd(op2_cmd) 
                exec_cmd(op3_cmd) 
            except:
                print('Wrong token')


        else:
            f.close()
    except FileNotFoundError:
        print('File CMD  does not exist')

    time.sleep(5)
