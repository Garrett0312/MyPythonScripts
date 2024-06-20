import csv
from itertools import zip_longest
import os
import tkinter as tk
import tkinter.filedialog

root = tk.Tk()
filename = tk.filedialog.askopenfilename()
root.destroy()

data = []

#file = open("C://Users/maxuser/Desktop/Sounding Txts/HRRR 3.9.23 15z F002.txt", "r")
file = open(filename)
filetitle = os.path.basename(filename)

data = []

while file:
   line = file.readline()
   for line in file:
       data.append(line)
   if line == "":
      break

file.close()
#print(data)

for i in data:
    #print(i)
    if "%RAW%" in i:
        S = data.index(i)+1
    if "%END%" in i:
        E = data.index(i)
dat = data[S:E]
lvls1 = []
for i in dat:
    lvls1.append((" ".join(i.split())))
g=[(i.split(',')) for i in lvls1]
sfc=g[1]

aux = []


for i in g:aux.append(abs(925-float(i[0])))
mb925=g[aux.index(min(aux))]
aux.clear()
for i in g:aux.append(abs(850-float(i[0])))
mb850=g[aux.index(min(aux))]
aux.clear()
for i in g:aux.append(abs(700-float(i[0])))
mb700=g[aux.index(min(aux))]
aux.clear()
for i in g:aux.append(abs(500-float(i[0])))
mb500=g[aux.index(min(aux))]
aux.clear()
for i in g:aux.append(abs(400-float(i[0])))
mb400=g[aux.index(min(aux))]
aux.clear()
for i in g:aux.append(abs(300-float(i[0])))
mb300=g[aux.index(min(aux))]
aux.clear()
for i in g:aux.append(abs(250-float(i[0])))
mb250=g[aux.index(min(aux))]
aux.clear()
for i in g:aux.append(abs(200-float(i[0])))
mb200=g[aux.index(min(aux))]
aux.clear()
for i in g:aux.append(abs(150-float(i[0])))
mb150=g[aux.index(min(aux))]
aux.clear()
for i in g:aux.append(abs(100-float(i[0])))
mb100=g[aux.index(min(aux))]


Tsfc = sfc[2]
Dsfc = sfc[3]
T925 = mb925[2]
D925 = mb925[3]
T850 = mb850[2]
D850 = mb850[3]
T700 = mb700[2]
D700 = mb700[3]
T500 = mb500[2]
D500 = mb500[3]
T400 = mb400[2]
D400 = mb400[3]
T300 = mb300[2]
D300 = mb300[3]
T250 = mb250[2]
D250 = mb250[3]
T200 = mb200[2]
D200 = mb200[3]
T150 = mb150[2]
D150 = mb150[3]
T100 = mb100[2]
D100 = mb100[3]


'''
print(sfc, Tsfc, Dsfc)
print(mb925,T925, D925)
print(mb850,T850, D850)
print(mb700,T700, D700)
print(mb500,T500, D500)
print(mb400,T400, D400)
print(mb300,T300, D300)
print(mb250,T250, D250)
print(mb200,T200, D200)
print(mb150,T150, D150)
print(mb100,T100, D100)
'''

#print("\n\n\n\n\n\n\n\n")
MSND = [Tsfc,Dsfc,T925,D925,T850,D850,T700,D700,T500,D500,T400,D400,T300,D300,T250,D250,T200,D200,T150,D150,T100,D100]
#print(MSND)


lvl = ['SFC',925,850,700,500,400,300,250,200,150,100]
Temps = [Tsfc,T925,T850,T700,T500,T400,T300,T250,T200,T150,T100]
Dews = [Dsfc,D925,D850,D700,D500,D400,D300,D250,D200,D150,D100]
snding = list(zip_longest(*[lvl,Temps,Dews]))

k = (os.path.splitext(filetitle)[0]).split( )
model = k[0]
date = k[1]
run = k[2]
fcsthr = k[3]

with open('//KGAN-TVDC-2/DigitalMedia/Custom/ImportedData/Manual Sounding.csv','w') as file:
    w = csv.writer(file)
    w.writerow(['Model Run',model+' '+run+' '+fcsthr+' '+date])
    w.writerow(['PRS','Temp','DewP'])
    w.writerows(zip_longest(*[lvl,Temps,Dews]))
    file.close()


print("Sounding data from:", model,date,run,fcsthr,'\n')
print(f"{'Level':<5}",f"{'Temp':^9}",f"{'DewPt':^11}")
for i in snding:
    print(f"{i[0]:>4}",f"{i[1]+chr(176)+'C':>9}",f"{i[2]+chr(176)+'C':>10}")
print('')
