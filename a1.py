import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare data
x = np.linspace(0, 10, 100) # Sample data from 0 to 10 with 100 points
y_linear = x
y_quadratic = x**2

# 2. Create a figure and axes using the object-oriented interface (recommended for complex plots)
fig, ax = plt.subplots(figsize=(8, 5)) # You can set the figure size here

# 3. Plot data on the axes
ax.plot(x, y_linear, label='linear', color='blue', linestyle='-') # Customize line properties
ax.plot(x, y_quadratic, label='quadratic', color='red', linestyle='--')

# 4. Add labels, title, and a legend
ax.set_xlabel('X-axis Label') # Add an x-label to the Axes
ax.set_ylabel('Y-axis Label') # Add a y-label to the Axes
ax.set_title('Simple Plot Example') # Add a title to the Axes
ax.legend() # Add a legend to explain the series
ax.grid(True) # Add gridlines for readability

# 5. Display the plot
plt.show() # Display the figure