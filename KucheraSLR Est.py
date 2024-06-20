import requests
from bs4 import BeautifulSoup
from datetime import date 
from datetime import datetime


today = date.today()
d5 = int(today.strftime("%y%m%d"))
utcget = str(datetime.utcnow())
c = (utcget.split(' '))
x = c[1].split(':')
utchr = int(x[0])
#print(utchr)
if utchr in range(3,7):
    current = str((d5+1))+"00"
elif utchr in range(7,13):
    current = str((d5))+"00"
else:
    current = str(d5)+"12"
#current = "22072400" #year_month_date_time

WFO = str.upper(input("What sounding site would you like? — Enter the WFO code:  \n\n\n\n\n"))
print('The current data is from the', WFO,current,'sounding','\n')
URL = 'https://www.spc.noaa.gov/exper/soundings/'+current+'_OBS/'+WFO+'.txt'
page = requests.get(URL)
soup = (BeautifulSoup(page.content, 'html.parser'))

f = (soup.get_text())

snd = (f[f.find("%RAW%")+6:f.find("%END%")]).split('\n')

data = []

for w in snd:
    data.append((w.split(',')))

sndslr = []
for i in data[1:len(data)-1]:
    sndslr.append([(float(x)) for x in i])

snd500 = [i for i in sndslr if i[0] >= 500]

tl500 = []
for i in snd500:
    tl500.append(i[2])
Tm = max(tl500)

if Tm < 4:
    #KUCHERA SLR CALCULATION
    
    TmK = (Tm + 273.15)
    
    if TmK > 271.16:
        SLR = round(12+2*(271.16-TmK),1)
    else:
        SLR = round(12+(271.16-TmK),1)
    
    print("The estimated Kuchera Snow/Liquid Ratio is",str(SLR)+":1")
else:
    print("Atmosphere is too warm for snow")