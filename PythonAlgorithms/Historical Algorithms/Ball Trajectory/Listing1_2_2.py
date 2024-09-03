import matplotlib.pyplot as plt
from Listing1_1 import ball_trajectory
xs = [x/100 for x in list(range(201))] #create an array of floating nums, 0.01 to 2.00
ys = [ball_trajectory(x) for x in xs] #apply trajectory algorithm of 0.01 to 2.00 in xs amt of times
xs2 = [0.1,2]
ys2 = [ball_trajectory(0.1),0]
xs3 = [0.2,2]
ys3 = [ball_trajectory(0.2),0]
xs4 = [0.3,2]
ys4 = [ball_trajectory(0.3),0]
plt.plot(xs,ys,xs2,ys2,xs3,ys3,xs4,ys4)
plt.title('The Trajectory of a Thrown Ball')
plt.xlabel('Horizontal Position of Ball')
plt.ylabel('Vertical Position of Ball')
plt.axhline(y=0)
plt.show()