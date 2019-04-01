import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40,c=y_values,cmap=(plt.cm.Blues),edgecolor=None)
plt.axis([0,1100,0,1100000])
# plt.show()
plt.savefig("squares_plot.png",bbox_inches="tight")
