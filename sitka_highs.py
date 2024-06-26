from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime



path = Path('weather_data/3653093.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# extract dates and high/low temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    try:
        high = int(row[12])
        low = int(row[14])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
print(highs)

# plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# format plot
ax.set_title("Daily High and Low Temeperatures, 2021\nDeath Valley, CA", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()