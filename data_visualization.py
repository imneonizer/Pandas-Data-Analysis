import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from itertools import cycle, islice

#input parameters================
file_name ='car_data.csv'
records = pd.read_csv(file_name)
df=pd.DataFrame(records)
#================================

unique_records = records['license_plates'].unique()

print(f'Total Visitors: {len(df)-1}')
print(f'Unique Visitors: {len(unique_records)}')
print()

data_mode = {}
for unique_rows in unique_records:
    idx = 1
    for any_rows in records['license_plates']:
        if unique_rows == any_rows:
            idx+=1
    data_mode.update({unique_rows:idx})

#sorting based on frequency for license plates
data_mode = sorted(data_mode.items(), key=lambda x: x[1], reverse=False)

number = []
frequency = []
colors = []
states = {}
for key,value in data_mode:
    number.append(key)
    frequency.append(value)

    options = [key]
    color = df.loc[df['license_plates'].isin(options)]
    color = list(color['colors'])[0]
    colors.append(color)

    options = [key]
    state = df.loc[df['license_plates'].isin(options)]
    state = list(state['states'])[0]
    states.update({state:value})

    #print(key, value)

unique_states = list(set(list(states.keys())))
unique_states_sorted = {}
for state in unique_states:
    unique_states_sorted.update({state:states[state]})

#sorting based on frequency for states
unique_states_sorted = sorted(unique_states_sorted.items(), key=lambda x: x[1], reverse=False)

state_list = []
state_frequency = []
for name, freq in unique_states_sorted:
    state_frequency.append(freq)
    state_list.append(name)
    #print(freq,name)


#sorting based on frequency for colors
colors_freq = {}
for unique_color in set(colors):
    idx = 1
    for color in colors:
        if unique_color == color:
            idx+=1
    colors_freq.update({unique_color:idx})

unique_colors_sorted = sorted(colors_freq.items(), key=lambda x: x[1], reverse=False)

color_list = []
color_frequency = []
for name, freq in unique_colors_sorted:
    color_frequency.append(freq)
    color_list.append(name)
    #print(freq,name)


#matplotlib.use('WebAgg') #using browser to visualize
plt.style.use('ggplot') #using ggplot style

#plotting colors data ==========================================================================
plt.figure('Colors') #plot name
plt.title('Analyzing Car Visiting Frequency Based on Colors')

#plt.plot(color_list, color_frequency, color='orange')

bar = plt.bar(color_list, color_frequency, label="Colors", color=color_list)
plt.xticks(rotation=90)

plt.xlabel('Colors')
plt.ylabel('Number of cars')

plt.tight_layout()
#plt.show()
#===============================================================================================

#plotting state data ==========================================================================
plt.figure('Location') #plot name
plt.title('Analyzing Car Visiting Frequency Based on Location')

plt.plot(state_list, state_frequency, color='orange')

bar = plt.bar(state_list, state_frequency, label="States", color='pink')
plt.xticks(rotation=90)

plt.legend()
plt.xlabel('From States')
plt.ylabel('Visiting Frequency')

plt.tight_layout()
#plt.show()
#===============================================================================================


#plotting license plate state data==============================================================
plt.figure('Number Plates') #plot name
plt.title('Analyzing Car Visiting Frequency Based on License Plates')

plt.plot(number,frequency, color='orange')

bar = plt.bar(number,frequency, label="Cars", color='pink')
plt.xticks(rotation=90)

plt.legend()
plt.xlabel('Number plates')
plt.ylabel('Visiting Frequency')

plt.tight_layout()
#plt.show()
#===============================================================================================

#showing all plots at once
plt.show()

