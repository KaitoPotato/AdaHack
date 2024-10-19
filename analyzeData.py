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

# Compare the number of incidents reported in each category (ADAS, ADS, Other)
incident_types = ['ADAS', 'ADS', 'Other']  # Category names
incident_counts = [len(adas_data_cleaned), len(ads_data_cleaned), len(other_data_cleaned)]  # Number of incidents in each category

# Create a bar plot showing the number of incidents by category
plt.figure(figsize=(8, 5))  # Set figure size
sns.barplot(x=incident_types, y=incident_counts, palette="coolwarm")  # Bar plot with custom color palette
plt.title('Number of Incidents by Category')  # Plot title
plt.xlabel('Incident Category')  # X-axis label
plt.ylabel('Number of Incidents')  # Y-axis label
plt.show()  # Display the plot

# Visualizing the top 10 reporting entities (who submitted the most reports) for each category
# Count the occurrences of each reporting entity and extract the top 10 most frequent ones
top_adas_entities = adas_data_cleaned['Reporting Entity'].value_counts().head(10)  # Top 10 reporting entities for ADAS
top_ads_entities = ads_data_cleaned['Reporting Entity'].value_counts().head(10)  # Top 10 reporting entities for ADS
top_other_entities = other_data_cleaned['Reporting Entity'].value_counts().head(10)  # Top 10 reporting entities for Other incidents

# Create a figure with 3 subplots, one for each category
plt.figure(figsize=(12, 8))  # Set figure size for all 3 subplots

# Plot for top ADAS reporting entities
plt.subplot(3, 1, 1)  # First subplot (1 out of 3)
sns.barplot(x=top_adas_entities.values, y=top_adas_entities.index, palette="Blues_d")  # Bar plot for ADAS with custom blue palette
plt.title('Top 10 Reporting Entities (ADAS)')  # Title for ADAS plot
plt.xlabel('Number of Reports')  # X-axis label
plt.ylabel('Reporting Entity')  # Y-axis label

# Plot for top ADS reporting entities
plt.subplot(3, 1, 2)  # Second subplot (2 out of 3)
sns.barplot(x=top_ads_entities.values, y=top_ads_entities.index, palette="Greens_d")  # Bar plot for ADS with custom green palette
plt.title('Top 10 Reporting Entities (ADS)')  # Title for ADS plot
plt.xlabel('Number of Reports')  # X-axis label
plt.ylabel('Reporting Entity')  # Y-axis label

# Plot for top Other incident reporting entities
plt.subplot(3, 1, 3)  # Third subplot (3 out of 3)
sns.barplot(x=top_other_entities.values, y=top_other_entities.index, palette="Reds_d")  # Bar plot for Other incidents with custom red palette
plt.title('Top 10 Reporting Entities (Other Incidents)')  # Title for Other plot
plt.xlabel('Number of Reports')  # X-axis label
plt.ylabel('Reporting Entity')  # Y-axis label

# Adjust the layout to avoid overlap of plot elements
plt.tight_layout()  # Prevent overlapping of subplots
plt.show()  # Display the entire figure with all 3 plots