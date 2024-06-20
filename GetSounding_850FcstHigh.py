import requests
from bs4 import BeautifulSoup
from datetime import date 
from datetime import datetime

today = date.today()
d5 = int(today.strftime("%y%m%d"))
utcget = str(datetime.utcnow())
c = (utcget.split(' '))
x = c[1].split(':')
utchr = x[0]
if utchr in range(3,15):
    current = str((d5+1))+"00"
else:
    current = str(d5)+"12"

URL = 'https://www.spc.noaa.gov/exper/soundings/'+current+'_OBS/DVN.txt'
page = requests.get(URL)
soup = (BeautifulSoup(page.content, 'html.parser'))
f = (soup.get_text())

snd = (f[f.find("%RAW%")+6:f.find("%END%")]).split('\n')

for i in snd:
    com = i.split(",")
    t = (com[0]).strip(' ')
    if '850.00' in t:
        q = i.split(',')
u = []
for i in q:
    u.append(float(i))
t850 = u[2]
tsfc = t850 + 15
Temp = round((tsfc*(9/5)+32))

print("Today's High will be around:",'%d\N{DEGREE SIGN}' "F" %Temp)
