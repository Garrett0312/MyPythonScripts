import requests
from bs4 import BeautifulSoup
import tkinter as tk
import csv


popup = tk.Tk()
popup.withdraw()
popup.lift()

WFO = (tk.simpledialog.askstring("NWS Weather Forecasting Office","Enter the NWS Weather Forecasting Office."
                                " (Enter <state> for list of WFOs by state, or <list> for all WFOs)")).title()

#WFO List on Garrett's Computer = 'C:\\Users\\gphey\Desktop\Programs\List of all NWS WFOs.csv'
#WFO List on Max Computer = 'C:\\Users\\maxuser\\Desktop\\Max Python Code\\List of all NWS WFOs.csv'
if len(WFO)>3:
    with open('C:/Users/maxuser/Desktop/Python Scripts/List of all NWS WFOs.csv', newline='') as f:
        reader = csv.reader(f)
        csvdata = list(reader)
        csvdata = csvdata[1:]
        print ("{:<4}|{:16}{:4}{:16}| {:>10}".format('WFO','','CITY','','STATE'))
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")
        if WFO != 'List':
            for i in csvdata:
                if WFO in i:
                    print("{:<4}|{:3}{:30}{:3}| {:>10}".format(i[0],'',i[1],'',i[2]))
                    print("------------------------------------------------------------")
                    continue
                    break
            WFO = (tk.simpledialog.askstring("NWS Weather Forecasting Office","Enter the NWS Weather Forecasting Office.\t\t\t\t\t\t\t")).title()

        if WFO =='List':
            for i in csvdata:
                print("{:<4}|{:3}{:>30}{:3}| {:>10}".format(i[0],'',i[1],'',i[2]))
                print("------------------------------------------------------------")
                #continue
            WFO = (tk.simpledialog.askstring("NWS Weather Forecasting Office","Enter the NWS Weather Forecasting Office.\t\t\t\t\t\t\t")).title()
    print("")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("")
    f.close()

#WFO = tk.simpledialog.askstring("NWS Weather Forecasting Office","Enter the NWS Weather Forecasting Office.\t\t\t\t\t\t\t")

URL = ('https://forecast.weather.gov/product.php?issuedby='+WFO+'&product=PFM&site='+WFO)

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
data = str(soup)


content = data[data.find('<!-- // CONTENT STARTS HERE -->'):data.find('</pre>')]
pfms = content.find('Point Forecast Matrices')
newdata = content[content.find('Point Forecast Matrices',pfms+1):]
datalst = newdata[newdata.find('Z')-2:]
loclist = (datalst.split('$$'))

#if City =="List":
s='-'
z='Z'
tab='\n'
upper = [0]
print(len(loclist)-1,"cities found")
for i in range(len(loclist)):
    state = (z.join(loclist[i].split(z)[-2:-1])[1:4])
    if i == 0:
        state = (z.join(loclist[i].split(z)[:-1])[:2])
    cities = (tab.join(loclist[i].split(s)[2:3]))
    if i == 0:
        cities = (s.join(loclist[i].split(s)[2:3]))
    if 'Elev.' in cities:
        print("")
        cities = (tab.join(loclist[i].split(tab)[2:3]))
        state = ""
    print((cities).title(),state)
    if cities.isupper():
        upper[0]=1
print("")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("")
City = tk.simpledialog.askstring("Local Forecast City", "Enter a city for the forecast for the area. \t\t\t\t\t\t\t")

if upper[0] == 0:
    City = City.title()
if upper[0] == 1:
    City = City.upper()

while True:
    if City not in data:
        City = tk.simpledialog.askstring("Location not in list", "Please use a major city in your county\t\t\t\t\t\t\t")
        City = City.title()
    else:
        break

if upper[0] == 0:
    City = City.title()
if upper[0] == 1:
    City = City.upper()

start = newdata.find(City)
end = newdata.find('$',start+1)
txt = newdata[start:end]
#print(txt)

#TimeCheck
times = (txt[(txt.find('3hrly')):(txt.find('UTC'))]).split()
time = list(map(int,(times[2:len(times)])))

tz = str(txt[(txt.find('3hrly')-4):(txt.find('3hrly')-1)])


for x in range(len(time)):
    if tz == 'EST':
        time[x] = time[x]-1
    elif tz =='CST':
        time[x]=(time[x])
    elif tz =='MST':
        time[x]=(time[x]+1)
    elif tz =='PST':
        time[x]=(time[x]+2)
    elif tz =='AKST':
        time[x]=(time[x]+3)
    elif tz =='HAST':
        time[x]=(time[x]+4)
    elif tz == 'EDT':
        time[x]=(time[x]-2)
    elif tz =='CDT':
        time[x]=(time[x]-1)
    elif tz =='MDT':
        time[x]=(time[x])
    elif tz =='PDT':
        time[x]=(time[x]+1)
    elif tz =='AKDT':
        time[x]=(time[x]+2)
    if tz =='HADT':
        time[x]=(time[x]+3)


#Hourly to 12 hour time

txtapm = txt[txt.find('ft'):txt.find('Date')]
apm = txtapm[txtapm.find('T')-5:txtapm.find('T')-3]
hr = txtapm[txtapm.find('ft')+2:txtapm.find('T')-6]
hr = round(int(hr),)
h = int(str(hr)[-2:])

if h > 30:
    hr = round((hr/100)+1,)
else:
    hr = round(hr/100,)

if apm == 'PM':
    if hr == 12:
        hr = hr
        hour = hr
    else:
        hr = hr+12
        hour = hr-12
else:

    if hr == 12:
        hr = 24
        hour = 12
    elif hr == 13:
        hr = 1
        hour = hr
    else:
        hr = hr
        hour = hr


if hr in range(1,4):
    hround = 3
if hr in range(4,7):
    hround = 6
if hr in range(7,10):
    hround = 9
if hr in range(10,13):
    hround = 12
if hr in range(13,16):
    hround = 15
if hr in range(16,19):
    hround = 18
if hr in range(19,22):
    hround = 21
if hr in range(22,25):
    hround = 0


if hround in range(0,6):
    tod1 = "Tonight"
    tod2 = "Tomorrow"
    hl1 = "low"
    hl2 = "high"
elif hround in range(15,25):
    tod1 = "Tonight"
    tod2 = "Tomorrow"
    hl1 = 'low'
    hl2 = 'high'
else:
    tod1 = "Today"
    tod2 = "Tonight"
    hl1 = "high"
    hl2 = 'low'



timenowcut = time.index(hround)
timenow = time[timenowcut:]


if hround in range (0,6):
    timeline = timenow.index(6,0,len(timenow))
elif hround in range(15,25):
    timeline = timenow.index(6,0,len(timenow))
else:
    timeline = timenow.index(18,0,len(timenow))

timeline12 = timeline+4


#State Find
statefind = (txt[(txt.find('Elev.'))-18:(txt.find('Elev.'))-16])


#Max/Min Temps
txtshort = (txt[txt.find(City):txt.find('Temp')])


minmax=''
if "Min/Max" in txtshort:
    minmax = (txtshort[txtshort.find('Min/Max'):txtshort.find('Temp')]).split()

if "Max/Min" in txtshort:
    minmax = (txtshort[txtshort.find('Max/Min'):txtshort.find('Temp')]).split()


txn1 = int(minmax[1])
txn2 = int(minmax[2])

#Wind Direction and Speed
windd = (txt[(txt.find('Wind dir')):txt.find('Wind spd')]).split()
winddir = windd[2:]
winds = (txt[txt.find('Wind spd'):txt.find('Clouds')]).split()
windspd = winds[2:]


for i in range(len(winddir)):
    if winddir[i] == 'N':
        winddir[i] = 'Northerly'
    elif winddir[i] == 'NE':
        winddir[i] = 'North Easterly'
    elif winddir[i] == 'E':
        winddir[i] = 'Easterly'
    elif winddir[i] == 'SE':
        winddir[i] = 'South Easterly'
    elif winddir[i] == 'S':
        winddir[i] = 'Southerly'
    elif winddir[i] == 'SW':
        winddir[i] = 'South Westerly'
    elif winddir[i] == 'W':
        winddir[i] = 'Westerly'
    if winddir[i] == 'NW':
        winddir[i] = 'North Westerly'
#print(winddir)

#Cloud Cover
cl = (txt[(txt.find('Clouds')):txt.find('PoP 12hr')]).split()
cloud = cl[1:]


clouds = []
#print(hround)
for i in range(len(cloud)):
    if cloud[i] == 'CL' and hround in range(0,6):
        clouds.append('Clear')
    elif cloud[i] == 'CL' and hround in range(12,25):
        clouds.append('Clear')
    elif cloud[i] == 'CL':
        clouds.append('Sunny')
    elif cloud[i] == 'FW' and hround in range(0,6):
        clouds.append('Mostly Clear')
    elif cloud[i] == 'FW' and hround in range(15,25):
        clouds.append('Mostly Clear')
    elif cloud[i] == 'FW':
        clouds.append('Mostly Sunny')
    elif cloud[i] == 'SC':
        clouds.append('Partly Cloudy')
    elif cloud[i] == 'B1' and hround in range(0,6):
        clouds.append('Partly Clear')
    elif cloud[i] == 'B1' and hround in range(15,25):
        clouds.append('Partly Clear')
    elif cloud[i] == 'B1':
        clouds.append('Partly Sunny')
    elif cloud[i] == 'B2':
        clouds.append('Mostly Cloudy')
    elif cloud[i] == 'OV':
        clouds.append('Cloudy')



#Chance of rain
pop = (txt[(txt.find('PoP 12hr')):(txt.find('QPF 12hr'))]).split()

#3 Hour Time Correction
ampm=[]
hrc=timenow

for y in timenow:
    if y == 0:
        ampm.append('AM')
    elif y < 12:
        ampm.append('AM')
    else:
        ampm.append('PM')

for x in range(len(timenow)):
    if timenow[x] == 0:
         hrc[x]=12
    if timenow[x] <= 12:
        hrc[x]=timenow[x]
    else:
        hrc[x]=timenow[x]-12

timecorrect = [None]*(len(hrc)+len(ampm))
timecorrect[::2] = hrc
timecorrect[1::2] = ampm

tc1 = (str(timecorrect[2]))+(str(timecorrect[3]))
tc2 = (str(timecorrect[4]))+(str(timecorrect[5]))
tc3 = (str(timecorrect[6]))+(str(timecorrect[7]))

#Temps 3 hours
hourlyT = (txt[(txt.find('Temp')):(txt.find('Dewpt'))]).split()


#Print the Forcast
print("Area forecast for",'%s'","%City.title(), statefind)
print("Forecasting Office:",WFO.upper())
print("Updated at", hour, apm,"CST")
print("")

print("Forecast for",'%s'":"%tod1)
print(clouds[timeline],"Skies")
print("with a", hl1, "of",'%d\N{DEGREE SIGN}' "F" %txn1)
print(winddir[timeline],"winds at",windspd[timeline],"MPH")
print("Chance of precip:",'%s%%' %pop[2])
print("")
print('%s'":"%tod2)
print(clouds[timeline12],"Skies")
print("with a", hl2,"of",'%d\N{DEGREE SIGN}' "F" %txn2)
print(winddir[timeline12],"winds at", windspd[timeline12], "MPH")
print("Chance of precip:",'%s%%' %pop[3])
print("")
print("Here are the conditions for the next 9 hours:")
print("At",tc1,"it will be",'%s\N{DEGREE SIGN}' "F" %hourlyT[1],
      "with",clouds[1],"skies.",winddir[1],"winds at",windspd[1],"MPH")
print("At",tc2,"it will be",'%s\N{DEGREE SIGN}' "F" %hourlyT[2],
      "with",clouds[2],"skies.",winddir[2],"winds at",windspd[2],"MPH")
print("At",tc3,"it will be",'%s\N{DEGREE SIGN}' "F" %hourlyT[3],
      "with",clouds[3],"skies.",winddir[3],"winds at",windspd[3],"MPH")
