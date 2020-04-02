import numpy as np
import pandas as pd
import html2text

from urllib.request import urlopen
from bs4 import BeautifulSoup

def html(link):
    html = urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')
    return soup
students=[]
link = input();
entry=html(link);

students=entry.find_all('div',{'class' : 'md-padding'})


for student in students :
    try:
        name = (student.find('a')).get_text()
        project=(student.find_all('div'))
        print(name,end="\t")
        print(project,end="\t")
    except Exception as error:
        print()
        
        
#this code is not complete it will run and do the scraping but cannot export results to csv file bu the output in terminal
#is really clean
