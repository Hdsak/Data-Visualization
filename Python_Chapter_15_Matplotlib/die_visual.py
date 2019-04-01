import matplotlib.pyplot as plt
import pygal
from die import Die

die_1=Die()
die_2=Die()
results=[]
for i in range(1000):
    results.append(die_1.roll()+die_2.roll())
frequences=[]
max_result=die_1.num_sides+die_2.num_sides
for i in range(2,max_result+1):
    frequences.append(results.count(i))
hist=pygal.Bar()
hist.title="Resul of rolling dice 1000 times"
hist.x_labels=[x for x in range(2,die_1.num_sides+die_2.num_sides)]
hist.x_title="Result"
hist.y_title="Frequncy of dice"
hist.add("Rolls d6 + d6",frequences)
hist.render_to_file("histo.svg")