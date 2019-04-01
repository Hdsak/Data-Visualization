import matplotlib.pyplot as plt
# 15-1. Кубы: число, возведенное в третью степень, называется «кубом».
#  Нанесите на диаграмму первые пять кубов, а затем первые 5000 кубов.
x_values=list(range(1,5000))
y_values=[x**3 for x in x_values]
print(y_values[5])
print(x_values[5])
plt.scatter(x_values,y_values,c=y_values,cmap=(plt.cm.Blues),edgecolors=None)
plt.show()
# 15-2. Цветные кубы: примените цветовую карту к диаграмме с кубами.