import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('afa2e701598d20110228 (1).csv', sep=';')

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# Basic statistics
print(df.describe())

# Plot trends over time for key parameters
plt.figure(figsize=(15, 10))
for i, param in enumerate(['NH4', 'BSK5', 'NO3', 'O2', 'Suspended']):
    plt.subplot(3, 2, i+1)
    for location in df['id'].unique():
        loc_data = df[df['id'] == location]
        plt.plot(loc_data['date'], loc_data[param], label=f'Location {location}')
    plt.title(param)
    plt.legend()
plt.tight_layout()
plt.show()

# Correlation analysis
corr_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Parameter Correlation Matrix')
plt.show()

# Identify extreme events
high_nh4 = df[df['NH4'] > 1]  # Threshold for ammonium pollution
high_no3 = df[df['NO3'] > 50]  # Threshold for nitrate pollution

print("High Ammonium Events:")
print(high_nh4[['id', 'date', 'NH4']].sort_values('NH4', ascending=False))

print("\nHigh Nitrate Events:")
print(high_no3[['id', 'date', 'NO3']].sort_values('NO3', ascending=False))
