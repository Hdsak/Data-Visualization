from matplotlib import pyplot as plt
import csv
from datetime import datetime

filename="death_valley_2014.csv"
with open(filename) as stast:
    reader=csv.reader(stast)
    header=next(reader)
    highs,lows,dates=[],[],[]
    for row in reader:
        try:
            high=int(row[1])
            date=datetime.strptime(row[0],"%Y-%m-%d")
            low=int(row[3])
        except ValueError:
            print(date," missing data")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.title("Dayly high and low temperatures - 2014",fontsize=20)
plt.xlabel("",fontsize=16)
plt.ylabel("Temperature",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=14)
fig.autofmt_xdate()
plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.1)
plt.show()