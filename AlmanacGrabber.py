import requests
import calendar
import math
from bs4 import BeautifulSoup
from datetime import datetime
from sys import exit
import tkinter as tk


URL = 'https://forecast.weather.gov/product.php?site=DVN&product=CLI&issuedby=CID'
#URL = 'https://forecast.weather.gov/product.php?site=DVN&issuedby=MLI&product=CLI&format=CI&version=2&glossary=0'


page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
data = str(soup)

content = data[data.find('CLIMATE REPORT'):data.find('$$')]
#print (content)
updated = content[(content.find('IL'))+2:(content.find('IL'))+9]
tod = content[(content.find('IL'))+7:(content.find('IL'))+9]

updated = updated[:2] + ":" + updated[2:]
up_date = content[(content.find('IL'))+14:(content.find('IL'))+30]


#print(content)

clocktime = datetime.now()

hour = int(clocktime.strftime('%H'))
mint = int(clocktime.strftime('%M'))
time = int(clocktime.strftime('%H%M'))
timestr = (str(hour)) + ":" + (str(mint))
sun = (content[content.find('SUNRISE AND SUNSET'):content.find('- INDICATES NEGATIVE NUMBERS.')]).split(' ')
sun[:] = (value for value in sun if value != '')
sun[5] = sun[5][:1]+':'+sun[5][1:]
sun[9] = sun[9][:1]+':'+sun[9][1:]
sun[14] = sun[14][:1]+':'+sun[14][1:]
sun[18] = sun[18][:1]+':'+sun[18][1:]


if tod == 'PM':
    #print("It's the evening")
    Tod = (content[content.find('TEMPERATURE (F)'):content.find('DEGREE DAYS')].split(' '))
    Tod[:] = (value for value in Tod if value != '')
    print("Here's the Alamanac for Today")
    print("")
    print("High:",Tod[4])
    print("Low:",Tod[13])
    print('Rain:',(Tod[28]))
    print('Month to Date:',(Tod[37]))
    if 'Snowfall:' in Tod:
        print('Snowfall:',(Tod[57]))
        print('Month to date:',(Tod[66]))
    print('Today:')
    print('Sunrise:',sun[5],sun[6],'','Sunset:',sun[9],sun[10])
    print('Tomorrow:')
    print('Sunrise:',sun[14],sun[15],'','Sunset:',sun[18],sun[19])
    print('')
else:
    #print("It's the morning")
    Yes = (content[content.find('TEMPERATURE (F)'):content.find('DEGREE DAYS')].split(' '))
    Yes[:] = (value for value in Yes if value != '')
    print("Here's the Alamanac for Yesterday")
    print("")
    print("High:",Yes[4])
    print("Low:",Yes[13])
    print('Rain:',(Yes[28]))
    print('Month to Date:',(Yes[37]))
    if 'Snowfall:' in Yes:
        print('Snowfall:',(Yes[57]))
        print('Month to date:',(Yes[66]))
    print('Today:')
    print('Sunrise:',sun[5],sun[6],'','Sunset:',sun[9],sun[10])
    print('Tomorrow:')
    print('Sunrise:',sun[14],sun[15],'','Sunset:',sun[18],sun[19])
    print("")

print('Updated at',updated,up_date)
#print(sun[14],sun[18])

#print('Sunrise:',sun[5],sun[6],'','Sunset:',sun[9],sun[10])