import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename="sitka_weather_2014.csv"
with open(filename) as weather:
    reader=csv.reader(weather)
    header_row=next(reader)
# for index,colum in enumerate(header_row):
#     print(index,colum)
    highs,lows,dates=[],[],[]
    for row in reader:
        dates.append(datetime.strptime(row[0],"%Y-%m-%d"))
        highs.append(int(row[1]))
        lows.append(int(row[2]))
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.title("Dayly high and low temperatures - 2014",fontsize=20)
plt.xlabel("",fontsize=16)
plt.ylabel("Temperature",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=14)
fig.autofmt_xdate()
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.show()