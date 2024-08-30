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

def checkToken():
    tokenfile= open(token_in_file, "r")
    client_str_cyper=tokenfile.readline()
    print(client_str_cyper )
    tokenfile.close()

    mypjwt=  PyJWT()
    client_str=mypjwt.decode(client_str_cyper , mysecret, options={'verify_signature': False, 'verify_exp': False,'verify_aud': False, 'verify_iss': False, 'verify_nbf' : False},algorithms=["HS256"])
    print(client_str )


if __name__ == '__main__':
    createToken()
    checkToken()
