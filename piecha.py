import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 30, 20, 25]  # Percentages
colors = ['red', 'yellow', 'pink', 'brown']
explode = (0.1, 0.2, 0, 0)  # Highlight the first slice (Apples)

# Create the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)

# Set aspect ratio to ensure the pie is circular
plt.axis('equal')

# Add a title
plt.title('Fruit Distribution')

# Display the chart
plt.show()
