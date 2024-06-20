import csv
#import json
from datetime import datetime
import arrow
from dateutil import tz
import requests
from time import sleep

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/Chicago')


while True:
    now = datetime.utcnow()
    date = str(now.strftime("%Y-%m-%d"))
    hour = int(now.strftime("%H"))
    
    options = {}
    options["url"] = "https://airnowapi.org/aq/data/"
    options["start_date"] = date
    options["start_hour_utc"] = str(hour-12)
    options["end_date"] = date
    options["end_hour_utc"] = str(hour)
    options["parameters"] = "pm25,pm10"
    options["bbox"] = "-91.773987,41.912237,-91.540527,42.053112"
    options["data_type"] = "b" #"a"
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
    #print(dat)
    #with open('C://Users/maxuser/Desktop/AQIdata2.txt', 'w') as f:
    #    json.dump(dat,f)
    #f.close()
    
    #with open ('C://Users/maxuser/Desktop/AQIdata2.txt','r') as f:
    #    data = json.load(f)
    
    
    t = []
    for i in data:
        tbreak = datetime.strptime(' '.join(i['UTC'].split('T')), '%Y-%m-%d %H:%M')
        upconv = tbreak.replace(tzinfo=from_zone)
        central = upconv.astimezone(to_zone)
        local = arrow.get(central).to('local').format('h A')
        t.append(local)
        t.append(str(i['AQI']))
    
    x = [t[i:i+2] for i in range(0, len(t), 2)]
    
    
    #f.close()
    
    with open('//KGAN-TVDC-2/DigitalMedia/Custom/ImportedData/AQI CID.csv','w') as file:
        w = csv.writer(file)
        w.writerow(['Time','AQI'])
        for i in x:
            w.writerow(i)
        file.close()
        
    if int(x[-1][1]) in range(0,51):
        aqitxt = "Good"
    elif int(x[-1][1]) in range(51,101):
        aqitxt = "Moderate"
    elif int(x[-1][1]) in range(101,151):
        aqitxt = "Unhealthy for Sensitive Groups"
    elif int(x[-1][1]) in range(151,201):
        aqitxt = "Unhealthy"
    elif int(x[-1][1]) in range(201,301):
        aqitxt = "Very Unhealthy"
    elif int(x[-1][1]) >300:
        aqitxt = "Hazardous"
    
    
    print('Cedar Rapids AQI updated at:', (datetime.now()).strftime("%I:%M %p, %B %d,%Y"))
    print('\n')
    print('The current AQI for Cedar Rapids is', x[-1][1]+',','which is',aqitxt)
    sleep(600) #Updates every 10 Minutes
