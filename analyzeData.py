import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV files
file_path_adas = '/Users/jack/Desktop/coding/AdaHack/SGO-2021-01_Incident_Reports_ADAS.csv'
file_path_ads = '/Users/jack/Desktop/coding/AdaHack/SGO-2021-01_Incident_Reports_ADS.csv'
file_path_other = '/Users/jack/Desktop/coding/AdaHack/SGO-2021-01_Incident_Reports_OTHER.csv'

# Reading the CSV files
adas_data = pd.read_csv(file_path_adas)
ads_data = pd.read_csv(file_path_ads)
other_data = pd.read_csv(file_path_other)

# Dropping columns with too many missing values (arbitrary threshold of 80% missing)
threshold = 0.8

# cleaning columns that have 20% data value missing, axis = 1 indicates working with columns
adas_data_cleaned = adas_data.dropna(thresh=int(threshold * len(adas_data)), axis=1)
ads_data_cleaned = ads_data.dropna(thresh=int(threshold * len(ads_data)), axis=1)
other_data_cleaned = other_data.dropna(thresh=int(threshold * len(other_data)), axis=1)

# Checking the structure of each dataset
adas_data_cleaned.columns, ads_data_cleaned.columns, other_data_cleaned.columns

# Compare the number of incidents reported in each category
incident_types = ['ADAS', 'ADS', 'Other']
incident_counts = [len(adas_data_cleaned), len(ads_data_cleaned), len(other_data_cleaned)]

plt.figure(figsize=(8, 5))
sns.barplot(x=incident_types, y=incident_counts)
plt.title('Number of Incidents by Category')
plt.ylabel('Number of Incidents')
plt.show()

# Visualizing top 10 reporting entities
top_adas_entities = adas_data_cleaned['Reporting Entity'].value_counts().head(10)
top_ads_entities = ads_data_cleaned['Reporting Entity'].value_counts().head(10)
top_other_entities = other_data_cleaned['Reporting Entity'].value_counts().head(10)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
sns.barplot(x=top_adas_entities.values, y=top_adas_entities.index)
plt.title('Top 10 Reporting Entities (ADAS)')

plt.subplot(3, 1, 2)
sns.barplot(x=top_ads_entities.values, y=top_ads_entities.index)
plt.title('Top 10 Reporting Entities (ADS)')

plt.subplot(3, 1, 3)
sns.barplot(x=top_other_entities.values, y=top_other_entities.index)
plt.title('Top 10 Reporting Entities (Other Incidents)')

plt.tight_layout()
plt.show()