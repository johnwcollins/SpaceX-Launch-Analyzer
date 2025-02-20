import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# Fetch from SpaceX API
url = "https://api.spacexdata.com/v4/launches"
response = requests.get(url)
launches = response.json()

launch_data = pd.DataFrame(launches)
launch_data = launch_data[['name', 'date_utc', 'success', 'rocket', 'launchpad', 'date_precision']]
#print(launch_data.head())

launch_data['date_utc'] = pd.to_datetime(launch_data['date_utc'])
launch_data['year'] = launch_data['date_utc'].dt.year

#print(launch_data.head())

success_rate = launch_data.groupby('year')['success'].mean() * 100
#print(success_rate)

sns.lineplot(x=success_rate.index, y=success_rate.values, marker='o')
plt.title('SpaceX Launch Success Rate Over Time')
plt.show()
