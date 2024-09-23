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
op4_cmd=[sys.executable, script_dir + 'training.py']
op5_cmd=[sys.executable, script_dir + 'validate.py']
op6_cmd=[sys.executable, script_dir + 'export.py']
nextphase_cmd=[sys.executable, script_dir+'sendstartcmd.py']

while True:
    try:
        f = open(file_cmd, "r")
        line=f.readline()
        if line.find("START")>-1 :
            f.close()        
            print("FIND CMD START")
            write_status("CLEAN DOWNLOAD DIR")
            exec_cmd(op1_cmd) 

            write_status("DOWNLOAD DATA")
            exec_cmd(download_cmd) 
            write_status("DOWNLOAD DATA EXECUTED")

            try:

                checkToken()

                write_status("CLEAN WORKING DIR")
                exec_cmd(op2_cmd) 
                exec_cmd(op3_cmd) 
                write_status("CLEAN WORKING DIR")

                write_status("TRAINING")
                exec_cmd(op4_cmd)
                write_status("TRAINING EXECUTED")

                write_status("VALIDATION")
                exec_cmd(op5_cmd) 
                write_status("VALIDATION EXECUTED")

                write_status("EXPORT")
                exec_cmd(op6_cmd) 
                write_status("EXPORT EXECUTED")

                createToken()

                write_status("SEND CMD NEXT PHASE")
                exec_cmd(nextphase_cmd) 
                write_status("SEND CMD NEXT PHASE EXECUTED")

            except:
                print('Wrong token')

        else:
            f.close()
    except FileNotFoundError:
        print('File CMD  does not exist')

    time.sleep(1)
