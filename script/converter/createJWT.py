#! /usr/bin/env python
import time
from config import *
from  jwtlib.api_jwt import PyJWT
from datetime import datetime, timedelta

def createToken():
    mypjwt=  PyJWT()

    ct_iat = datetime.now()
    ct_exp = datetime.now()+timedelta(1)
    ts_iat=ct_iat.timestamp()
    ts_exp=ct_exp.timestamp()

    header={"typ" : "JWT","alg": "HS256"}
    mypayload={"exp":0,"iat":0,"iss":"augmentor","cmd": "start","aud":"https://172.10.0.3/cgi-bin/startcmd.py"}
    mypayload["exp"]=ts_exp
    mypayload["iat"]=ts_iat
    print(mypayload)
    client_str_cyper  = mypjwt.encode(payload=mypayload, key=mysecret,headers=header, algorithm="HS256")
    print(client_str_cyper )
    tokenfile= open(token_out_file, "w")
    tokenfile.writelines(client_str_cyper)
    tokenfile.close()

if __name__ == '__main__':
    createToken()
