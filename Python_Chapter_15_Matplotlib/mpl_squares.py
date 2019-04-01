import matplotlib.pyplot as plt
squares=[1,4,9,16,25]
input_values=[1,2,3,4,5]
plt.plot(input_values,squares,linewidth=5)
plt.title("Square Number",fontsize=25)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis="both",labelsize=15)
plt.scatter(2,5)

plt.show()