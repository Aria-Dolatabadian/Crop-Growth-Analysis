import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read data from CSV file
data = pd.read_csv('crop_data.csv')
# Calculate RGR
data['RGR'] = (np.log(data['Weight']) - np.log(data['Weight'].shift(1))) / (data['Day'] - data['Day'].shift(1))
# Calculate rolling average of RGR
data['RGR_smooth'] = data['RGR'].rolling(window=3, center=True).mean()
# Visualize the results
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Day')
ax1.set_ylabel('Weight', color=color)
ax1.plot(data['Day'], data['Weight'], color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('RGR', color=color)
ax2.plot(data['Day'], data['RGR'], color=color, alpha=0.5, label='RGR')
ax2.plot(data['Day'], data['RGR_smooth'], color='purple', label='Smoothed RGR')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(bbox_to_anchor=(1, 0.5))
plt.title('Crop Growth Analysis')
plt.show()
# Export the data
data.to_csv('RGR_data.csv', index=False)






# Set up parameters
start_day = 1
end_day = 180
initial_weight = 10 # gram per meter square
mean_growth_rate = 5 # gram per meter square per day
std_dev_growth_rate = 1 # gram per meter square per day
# Read data from CSV file
data = pd.read_csv('crop.csv')
# Calculate CGR
data['CGR'] = (data['Weight'] - initial_weight) / (data['Day'] - start_day)
# Visualize the results
fig, ax = plt.subplots()
ax.set_xlabel('Day')
ax.set_ylabel('Weight')
ax.plot(data['Day'], data['Weight'], label='Crop Weight')
ax2 = ax.twinx()
ax2.set_ylabel('CGR (gm m-2 day-1)')
ax2.plot(data['Day'], data['CGR'], color='red', label='CGR')
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper center')
plt.title('Crop Growth Analysis')
# # Export the data
data.to_csv('CGR_data.csv', index=False)
plt.show()




import pandas as pd
import matplotlib.pyplot as plt
# Set up parameters
start_day = 1
end_day = 180
initial_leaf_area = 10 # m^2
mean_growth_rate = 0.1 # m^2 per day
std_dev_growth_rate = 0.02 # m^2 per day
# Read data from CSV file
data = pd.read_csv('leaf_area_data.csv')
# Calculate LAI
ground_area = 100 # m^2
data['LAI'] = 2 * data['Leaf Area'] / ground_area
# Visualize the results
fig, ax = plt.subplots()
ax.set_xlabel('Day')
ax.set_ylabel('Leaf Area (m$^2$)')
ax.plot(data['Day'], data['Leaf Area'])
ax2 = ax.twinx()
ax2.set_ylabel('LAI')
ax2.plot(data['Day'], data['LAI'], color='red')
plt.title('Leaf Area Index Analysis')
data.to_csv('LAI.csv', index=False)
plt.show()



