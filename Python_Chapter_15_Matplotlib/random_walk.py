from random import choice

class RandomWalk():
    """Class for random walking"""
    def __init__(self,num_points=5000):
        self.num_points=num_points
        """All attr starts in 0,0"""
        self.x_values=[0]
        self.y_values=[0]
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            next_x=self.x_values[-1]+self.get_step()
            next_y=self.y_values[-1]+self.get_step()
            self.x_values.append(next_x)
            self.y_values.append(next_y)
    def get_step(self):
             """Define direction and length of movement"""
             direction=choice([1,-1])
             distance=choice([0,1,2,3,4])
             step=direction*distance
             return step

