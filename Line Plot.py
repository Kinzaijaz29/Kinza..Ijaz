# -*- coding: utf-8 -*-
"""
Sunshine Comparison Plot

This program generates a line plot to compare the duration of bright sunshine in Scotland for the years 2021, 2022, and 2023. It uses Matplotlib for data visualization and presents the data as a line plot with data points for each month.

Author: kinza Ijaz
Date: [Sun Nov  5 23:17:57 2023]

"""
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
data = pd.read_csv("/Users/Ammad computer/Documents/bright sunshine.csv")

x = data.months
y = data.sunshine_in_2021
z = data.sunshine_in_2022
v = data.sunshine_in_2023

#Label the plot
plt.xlabel('months')
plt.ylabel('sunshine')

plt.plot(x, y, label='Sunshine in 2021', marker='o',markerfacecolor='green')
plt.plot(x, z, label='Sunshine in 2022', marker='o',markerfacecolor='green')
plt.plot(x,v, label='Sunshine in 2023', marker='o',markerfacecolor='green')

#Add Title
plt.title('Sunshine comparison in past 3 years')
plt.legend()

plt.show()

