import plotly

# Creating the Die Class
from random import randint

class Die:
    """A class representing a single die"""

    def __init__(self, num_sides=6):    # Default number of sides is 6
        self.num_sides = num_sides

    def roll(self):     # Roll() method uses the randint() function to return a random number between 1 and the number of sides
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)

# Rolling one Die
from die import Die
die = Die()

results = []    # Create empty list to store results
for roll_num in range(100):     # Roll die 100 times, store results in our list
    result = die.roll()
    results.append(result)

print(results)

# Analyzing the Results
frequencies = []
for value in range(1, die.num_sides+1):     # Count each time a number appears in the results
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Making a Histogram
""" A Histogram is a bar chart showing how often certain results occur"""
from plotly.graph_objs import Bar, Layout
from plotly import offline

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]     # Bar() class represents a data set that will be formatted as a bar chart, needs x and y values as input

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 100 times', xaxis=x_axis_config, yaxis=y_axis_config)# Layout() class specifies layout and configuration of chart as a whole
offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')     # Generates the plot


# Rolling Two Dice
"""
from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()    # Calculate sum of both rolls
    results.append(result)


# Analyzing the Results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides  # Max result of both sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_results+1))     # Results of both rolls on X axis
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result', 'dtick':1}       # dtick controls the spacing between tick marks
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 100 times', xaxis=x_axis_config, yaxis=y_axis_config)# Layout() class specifies layout and configuration of chart as a whole
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d6.html')     # Generates the plot
"""
