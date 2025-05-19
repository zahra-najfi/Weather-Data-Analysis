import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV
df = pd.read_csv("weather_data.csv")

# Step 2: Clean Data
df = df.dropna(subset=['City'])  # Remove rows without city
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert to datetime
df = df.dropna(subset=['Date'])  # Remove invalid dates
df = df.sort_values('Date')      # Sort by date

# Step 3: Plot
plt.figure(figsize=(12, 6))

for city in df['City'].unique():
    city_data = df[df['City'] == city]
    plt.plot(city_data['Date'], city_data['MaxTemp'], label=f'{city} MaxTemp')
    plt.plot(city_data['Date'], city_data['MinTemp'], label=f'{city} MinTemp')

# Step 4: Format Plot
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Daily Max/Min Temperature Trends")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

