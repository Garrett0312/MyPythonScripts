import csv
#import json
from datetime import datetime, timedelta
import arrow
from dateutil import tz
import requests
#from time import sleep



from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/Chicago')


#while True:


Cities = {'CID': '-91.773987,41.912237,-91.540527,42.053112','ALO': '-92.501831,42.366403,-92.125549,42.583164',\
          'DBQ': '-91.021423,42.335956,-90.458374,42.708421','IOW': '-91.710429,41.563825,-91.411052,41.760808'}
cidfull = []
alofull = []
dbqfull = []
iowfull = []

#Get AQI Data one city at a time
for i in Cities:
    now = datetime.utcnow()
    dateend = str(now.strftime("%Y-%m-%d"))
    hourend = int(now.strftime("%H"))
    d = datetime.utcnow() - timedelta(hours=6, minutes=0)
    datestart = str(d.strftime("%Y-%m-%d"))
    hourstart = str(d.strftime("%H"))
    options = {}
    options["url"] = "https://airnowapi.org/aq/data/"
    options["start_date"] = str(datestart)
    options["start_hour_utc"] = str(hourstart)
    options["end_date"] = str(dateend)
    options["end_hour_utc"] = str(hourend)
    options["parameters"] = "pm25,pm10,ozone"
    #options["bbox"] = "-91.773987,41.912237,-91.540527,42.053112"
    options["bbox"] = Cities[i]
    options["data_type"] = "A" #"a"
    options["format"] = "application/json"
    options["api_key"] = "98442F66-BF8D-4A23-AD34-90A9E18A4E7F"
    
    # API request URL
    URL = options["url"] \
                  + "?startdate=" + options["start_date"] \
                  + "t" + options["start_hour_utc"] \
                  + "&enddate=" + options["end_date"] \
                  + "t" + options["end_hour_utc"] \
                  + "&parameters=" + options["parameters"] \
                  + "&bbox=" + options["bbox"] \
                  + "&datatype=" + options["data_type"] \
                  + "&format=" + options["format"] \
                  + "&api_key=" + options["api_key"]
    response = requests.get(URL)
    data= response.json()
    
    #Build Cedar Rapids AQI Data
    if i == "CID":
        h=[]
        g=[]
        cidAQI=[]
        for s in data:
            if s['Parameter'] == 'OZONE':
                cidfull.append(s)
            elif s['Parameter'] == 'PM2.5':
                cidfull.append(s)
            elif s['Parameter'] == 'PM10':
                cidfull.append(s)
        for i in cidfull:
            if i['UTC'] not in h:
                h.append(i['UTC'])
        for i in h:
            u=[]
            u.append(i)
            for j in cidfull:
                if(j['UTC']==i):
                    u += j['Parameter'],j['AQI']
            g.append(u)
        for i in g:
            #print(i)
            if len(i)==7:
                cidAQI.append([i[0],i[(i.index(max(i[2],i[4],i[6])))-1],max(i[2],i[4],i[6])])
            if len(i)==5:
                cidAQI.append([i[0],i[(i.index(max(i[2],i[4])))-1],max(i[2],i[4])])
            if len(i) ==3:
                cidAQI.append([i[0],i[1],i[2]])
    
    #Build Waterloo AQI Data
    elif i == "ALO":
        h=[]
        g=[]
        aloAQI=[]
        for s in data:
            if s['Parameter'] == 'OZONE':
                alofull.append(s)
            elif s['Parameter'] == 'PM2.5':
                alofull.append(s)
            elif s['Parameter'] == 'PM10':
                alofull.append(s)
        for i in alofull:
            if i['UTC'] not in h:
                h.append(i['UTC'])
        for i in h:
            u=[]
            u.append(i)
            for j in alofull:
                if(j['UTC']==i):
                    u += j['Parameter'],j['AQI']
            g.append(u)
        for i in g:
            if len(i)==7:
                aloAQI.append([i[0],i[(i.index(max(i[2],i[4],i[6])))-1],max(i[2],i[4],i[6])])
            if len(i)==5:
                aloAQI.append([i[0],i[(i.index(max(i[2],i[4])))-1],max(i[2],i[4])])
            if len(i) ==3:
                aloAQI.append([i[0],i[1],i[2]])
    
    #Build Dubuque AQI Data
    elif i=="DBQ":
        h=[]
        g=[]
        dbqAQI=[]
        for s in data:
            if s['Parameter'] == 'OZONE':
                dbqfull.append(s)
            elif s['Parameter'] == 'PM2.5':
                dbqfull.append(s)
            elif s['Parameter'] == 'PM10':
                dbqfull.append(s)
        for i in dbqfull:
            if i['UTC'] not in h:
                h.append(i['UTC'])
        for i in h:
            u=[]
            u.append(i)
            for j in dbqfull:
                if(j['UTC']==i):
                    u += j['Parameter'],j['AQI']
            g.append(u)
        for i in g:
            if len(i)==7:
                dbqAQI.append([i[0],i[(i.index(max(i[2],i[4],i[6])))-1],max(i[2],i[4],i[6])])
            if len(i)==5:
                dbqAQI.append([i[0],i[(i.index(max(i[2],i[4])))-1],max(i[2],i[4])])
            if len(i) ==3:
                dbqAQI.append([i[0],i[1],i[2]])
    
    #Build Iowa City AQI Data
    elif i=="IOW":
        h=[]
        g=[]
        iowAQI=[]
        for s in data:
            if s['Parameter'] == 'OZONE':
                iowfull.append(s)
            elif s['Parameter'] == 'PM2.5':
                iowfull.append(s)
            elif s['Parameter'] == 'PM10':
                iowfull.append(s)
        for i in iowfull:
            if i['UTC'] not in h:
                h.append(i['UTC'])
        for i in h:
            u=[]
            u.append(i)
            for j in iowfull:
                if(j['UTC']==i):
                    u += j['Parameter'],j['AQI']
            g.append(u)
        for i in g:
            if len(i)==7:
                iowAQI.append([i[0],i[(i.index(max(i[2],i[4],i[6])))-1],max(i[2],i[4],i[6])])
            if len(i)==5:
                iowAQI.append([i[0],i[(i.index(max(i[2],i[4])))-1],max(i[2],i[4])])
            if len(i) ==3:
                iowAQI.append([i[0],i[1],i[2]])

#Remove any missing data from lists
for i in cidAQI:
    if i[2]==-999:
        print('CID missing data at',cidAQI[cidAQI.index(i)][0],'- removed from feed')
        del cidAQI[cidAQI.index(i)]
for i in aloAQI:
    if i[2]==-999:
        print('ALO missing data at',aloAQI[aloAQI.index(i)][0],'- removed from feed')
        del aloAQI[aloAQI.index(i)]
for i in dbqAQI:
    if i[2]==-999:
        print('DBQ missing data at',dbqAQI[dbqAQI.index(i)][0],'- removed from feed')
        del dbqAQI[dbqAQI.index(i)]
for i in iowAQI:
    if i[2]==-999:
        print('IOW missing data at',iowAQI[iowAQI.index(i)][0],'- removed from feed')
        del iowAQI[iowAQI.index(i)]


print('\n\n')
#Humanizes the date/time to just the time
cidAQI[-1][0] = arrow.get(((datetime.strptime(' '.join(cidAQI[-1][0].split('T')), '%Y-%m-%d %H:%M'))\
                   .replace(tzinfo=from_zone)).astimezone(to_zone)).to('local').format('h A')
aloAQI[-1][0] = arrow.get(((datetime.strptime(' '.join(aloAQI[-1][0].split('T')), '%Y-%m-%d %H:%M'))\
                   .replace(tzinfo=from_zone)).astimezone(to_zone)).to('local').format('h A')
dbqAQI[-1][0] = arrow.get(((datetime.strptime(' '.join(dbqAQI[-1][0].split('T')), '%Y-%m-%d %H:%M'))\
                   .replace(tzinfo=from_zone)).astimezone(to_zone)).to('local').format('h A')
iowAQI[-1][0] = arrow.get(((datetime.strptime(' '.join(iowAQI[-1][0].split('T')), '%Y-%m-%d %H:%M'))\
                   .replace(tzinfo=from_zone)).astimezone(to_zone)).to('local').format('h A')


allAQI = {'CID':cidAQI[-1],'ALO':aloAQI[-1],'DBQ':dbqAQI[-1],'IOW':iowAQI[-1]}


print('{:4}  {:11}  {:4}  {:5}'.format('City','Last Update','AQI','Pollutant'))
for i in allAQI:
    print('{:>4}  {:>8}  {:6}  {:>8}'.format(i,allAQI[i][0],allAQI[i][2],allAQI[i][1]))

#write to CSV file for Max
with open('//KGAN-TVDC-2/DigitalMedia/Custom/ImportedData/AQI Multi.csv','w') as file:
    w = csv.writer(file)
    w.writerow(['City','Last Update','AQI','Pollutant'])
    for i in allAQI:
        w.writerow([i,allAQI[i][0],allAQI[i][2],allAQI[i][1]])
    file.close()

    #sleep(5) #Updates every 10 Minutes
