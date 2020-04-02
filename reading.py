import json
import requests
import string as str
import csv

def oneword(str):
    for x in range(len(str)):
        if str[x]==32 :
            flag2=1

flag0=0
flag1=0
flag2=0

jfile = input('Enter json file path : ')
j=open(jfile)
jdata = json.load(j)
for data in jdata : 
    print(data['n'],end=" ")
    print(data['i'],end=" ")
    print(data['p'])