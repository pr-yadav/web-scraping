import json
import requests
import string as str
import csv


#func to check for space between name
def oneword(str):
    for x in range(len(str)):
        if str[x]==32 :
            flag2=0

#function to check for special char
def specialchar(str):
    for x in range(len(str)):
        if not((str[x]>='A' and str[x]<="Z")or(str[x]>='a' and str[x]<='z')) :
            flag1=1

flag1=0
flag2=1
str={}


#taking input and printing invalid names
#-----------------------------------------------------------------

jfile = input('Enter json file path : ')
cfile = input('Enter csv file path : ')
with open(cfile, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        str=row[0]
        oneword(row[0])
        specialchar(row[0])
        if ((row[0]).islower() or not flag2  or flag1):
            print(row[0])
        flag1=0
        flag2=1
#-----------------------------------------------------------------
#assuming the format of csv file to be name(row[0]);organization(row[1]);project[row(2)]


#printing the data

j=open(jfile)
jdata = json.load(j)
for data in jdata : 
    print(data['n'],end=" ")
    print(data['i'],end=" ")
    print(data['p'],end=" ")
    with open(cfile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if data['n']==row[0] :
                print(row[1] ,end=" ")
                print(row[2])
    print()


#--------------------------------------------------
