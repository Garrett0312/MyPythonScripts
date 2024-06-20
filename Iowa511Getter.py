from datetime import datetime, timedelta
import requests
import csv
from time import sleep


while True:
    url = "https://services.arcgis.com/8lRhdTsQyJpO52F1/arcgis/rest/services/CARS511_Iowa_View/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    response = requests.get(url)
    
    f= response.json()
    
    
    now = datetime.now()
    fnow = now.strftime('%Y-%m-%d %H:%M:%S')
    tnow = datetime.strptime(fnow, '%Y-%m-%d %H:%M:%S')
    
    causelist = ['due to stalled vehicle. ','due to crash. ','due to emergency repairs. ','due to multi vehicle crash. ']
    eventlist=[]
    eventlst=[]
    count=0
    
    
    for i in f['features']:
        #upd = str(i['attributes']['IssueDate'])+str(i['attributes']['IssueTime'])
        #tbreak = datetime.strptime(upd, '%Y%m%d%H%M%S')
        upd = i['attributes']['gisupdated']
        tbreak = datetime.strptime(upd, '%Y%m%d %H%M%S')
        timebreak = tnow - tbreak
        stnum = 1000
        if timebreak < timedelta(hours=1,minutes=0):
            count = count+1
            if i['attributes']['cause'] in causelist:
                if i['attributes']['cause'] == 'due to stalled vehicle. ':
                    stnum = -1
                elif i['attributes']['cause'] == 'due to emergency repairs. ':
                    stnum = -1
                elif i['attributes']['cause'] == 'due to crash. ':
                    stnum = 1
                elif i['attributes']['cause'] == 'due to multi vehicle crash. ':
                    stnum = 2
                eventlst.append([i['geometry']['y'],i['geometry']['x'],stnum,i['attributes']['phrase'],\
                                  i['attributes']['cause']])
    
    for elem in eventlst:
        if elem not in eventlist:
            eventlist.append(elem)
    
    
    count = 0
    for i in eventlist:
        count = count+1
        i.insert(0, count)
        i.insert(0, count)
    
    for i in eventlist:
        print(i)
    
    listlen = len(eventlist)
    for listlen in range(listlen,100):
        listlen = listlen+1
        eventlist.append([listlen,listlen,0.00000000000000,0.000000000000000000000,99999,'None,','None'])
       
    
    
    with open('//KGAN-TVDC-2/DigitalMedia/Custom/NavImportedData/Iowa511.csv','w') as file:
        w = csv.writer(file)
        w.writerow(["Loc ID",'Time','lat','long','iconvalue','phrase','cause'])
        for i in eventlist:
            w.writerow(i)
        file.close()
    
    print('\n\n')
    sleep(60)