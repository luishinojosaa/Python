# A Random Walk is a path that has no clear direction but is determined by a series of random decisions, each of which is left entirely to chance

# Creating the Random Walk
from random import choice

class RandomWalk:

    def __init__(self, num_points=5000):        # Set default number of points in a walk to 5000
        # Initialize attributes of a walk
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

# Choosing Directions
    def fill_walk(self):
            # Calculate all the points in a walk

            # Keep taking steps until the walk reaches the desired length
            while len(self.x_values) < self.num_points:         # Set up loop to run until walk is filled with correct number of points

                # Decide which direction to go and how far to go
                x_direction = choice([1, -1])       # Returns either 1 for right movement, or -1 for left movement
                x_distance = choice([0, 1, 2, 3, 4])    # Tells Python how far to move in that direction (x_distance) randomly (between 0 and 4)
                x_step = x_direction * x_distance       # Determine length of each step by multiplying direction of movement by the distance
                                                        # A positive result means move right, negative means move left, and 0 means move vertically
                y_direction = choice([1, -1])
                y_distance = choice([0, 1, 2, 3, 4])
                y_step = y_direction * y_distance       # A positive result means move up, negative means move down, 0 means it goes nowhere

                # Reject moves that go nowhere
                if x_step ==0 and y_step == 0:          # Loop continues if we move nowhere
                    continue

                # Calculate the new position
                x = self.x_values[-1] + x_step      # Add new value to last stored value in x_value/y_value
                y = self.y_values[-1] + y_step

                self.x_values.append(x)
                self.y_values.append(y)


                

# Plotting the Random walk
import matplotlib.pyplot as plt
from random_walks import RandomWalk

# Keep making new walks, as long as program is active
""" while True: """

# Make a Random walk
rw = RandomWalk()       # To have different number of plot points, put number in parenthesis RandomWalk(50_000), but remember to adjust size of points
rw.fill_walk()

# Plot the points in the walks
plt.style.use('classic')
fig, ax = plt.subplots()

point_numbers = range(rw.num_points)        # Use range to generage lsit of numbers equal to number of points on the walk

ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)   # Use color map to show order of points plotted

# Emphasize the first and last points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)       # Starting point at 0,0
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)     # Ending point

# Remove axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

"""
keep_running = input("Make another walk? (y/n): ")
if keep_running == 'n':
    break
"""
