import requests
from bs4 import BeautifulSoup

#url = https://mesonet.agron.iastate.edu/GIS/apps/rview/warnings.phtml
URL = 'https://mesonet.agron.iastate.edu/GIS/apps/rview/warnings.phtml'
page = requests.get(URL)
soup = (BeautifulSoup(page.content, 'html.parser'))
f = (soup.get_text())
# = soup.get

#print(f)

content = f[f.find('Warnings Valid at:'):f.find('Download GIS shapefile of current warnings')]
#print(type(content))
#print(content.split('\n'))
t=content.split('\n')
#print(t)
IAWarn = []
for i in t:
    #print(i,'\n')
    if i[0:2] == 'IA':
        IAWarn.append(i[2:])

print('########################')
#print(t[1][2:])
e=t[1][2:]
print(e)
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
#y=e[e.find('expires'):e.find(' by ')-9]
y = [e[:e.find('(View Text)')-1],[e[e.find('expires'):e.find(' by ')-9],e[e.find('expires')+8:e.find(' by ')]],\
     [e[e.find('Issued:'):e.find('Issued:')+6],e[e.find('Issued:')+8:e.find('Updated')]]]
print(y)
print('########################')
for i in IAWarn:
    print(i,'\n')
#for i in content:
#    warn.append(i.split('\n'))

#print(warn) by MTR 
