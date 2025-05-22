import numpy as np
import matplotlib.pyplot as plt

# This code generates a sine wave using numpy and matplotlib.

x_data1 = np.linspace(0, 10*np.pi, 1000)
y_data1 = np.sin(x_data1)

plt.plot(x_data1, y_data1)
plt.title("Sine Wave")
plt.xlabel("X_data")
plt.ylabel("Y_data")
plt.show() # show the plot, window might not pop up if you didn't run this in a script

# let us now plot a scatter plot

x_data2 = np.random.uniform(0,1,100)
y_data2 = np.random.uniform(0,1,100)

plt.scatter(x_data2, y_data2)
plt.title("Scatter plot")     
plt.xlabel("X_data")
plt.ylabel("Y_data")
plt.show()

