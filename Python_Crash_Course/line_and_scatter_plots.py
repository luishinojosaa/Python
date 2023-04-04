#This is a test
#  ---------- Plotting a Simple Line Graph ------------------
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()    # subplots() generates one or more plots in the same figure, fig represents the entire figure of plots that are generated

ax.plot(squares)    # plot() method will plot data in a meaningful way

plt.show()

# ---------- Changing the Label Type and Line Thickness ------------------
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

ax.plot(squares)

plt.show()

# ---------- Correcting the Plot ------------------
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()

# ---------- Using Built-in Styles ------------------
import matplotlib.pyplot as plt
x = plt.style.available
print(x)
# 'Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale',
# 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
# 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'

# ---------- Plotting and Styleing Individual Points with scatter() ------------------
import matplotlib.pyplot as plt

plt.style.use('seaborn')

fig, ax = plt.subplots()

ax.scatter(2, 4)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()

# ---------- Plotting a Series of Points with scatter() ------------------
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=100)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()

# ---------- Calculating Data Automatically ------------------

import matplotlib.pyplot as plt

x_values = range(1, 1001)       # Automatically calculate values using range()
y_values = [x**2 for x in x_values] # Calculate square values

plt.style.use('seaborn')        # Declare style

fig, ax = plt.subplots()    # Declare figure

ax.scatter(x_values, y_values, s=10)

ax.axis([0, 1100, 0, 1100000])  # Setting Axis values axis([x lower, x upper, y lower, y upper])

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()

# ---------- Custom Colors & Colormaps ------------------

ax.scatter(x_values, y_values, c='red', s=10)   # Pass c to scatter with name of colorblind

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # Colormaps are a series of colors in a gradient that move from a starting to ending color

# ---------- EXERCISE / Plot the first five cubic numbers, and then plot the first 5000 cubic numbers  ------------------

import matplotlib.pyplot as plt

x_values = range(1, 5001)       # Automatically calculate values using range()
y_values = [x**3 for x in x_values] # Calculate square values

plt.style.use('seaborn')        # Declare style

fig, ax = plt.subplots()    # Declare figure

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# ax.axis([0, 6, 0, 140])  # Setting Axis values axis([x lower, x upper, y lower, y upper])

ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()
