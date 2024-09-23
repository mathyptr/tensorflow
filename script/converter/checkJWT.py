#! /usr/bin/env python
import time
from config import *
from  jwtlib.api_jwt import PyJWT
from datetime import datetime, timedelta


tokenfile= open(token_in_file, "r")
client_str_cyper=tokenfile.readline()
print(client_str_cyper )
tokenfile.close()

mypjwt=  PyJWT()
client_str=mypjwt.decode(client_str_cyper , mysecret, options={'verify_signature': False, 'verify_exp': False,'verify_aud': False, 'verify_iss': False, 'verify_nbf' : False},algorithms=["HS256"])
print(client_str )
