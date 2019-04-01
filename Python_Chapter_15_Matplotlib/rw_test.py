import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw=RandomWalk(5000)
    rw.fill_walk()
    #plt.figure(figsize=(10,6))
    points=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=points,cmap=plt.cm.Blues,s=1,edgecolors=None)
    plt.scatter(0,0,c='green',s=100,edgecolors=None)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100,edgecolors=None)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    # flag=input("Keep? ")
    # if flag=='n':
    #     break
    break