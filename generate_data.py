import pandas as pd
import random

#  "Fake" Dataset simulating a messy CSV file
raw_data = {
    "Player": ["LeBron James", "Steph Curry", "Kevin Durant", "LeBron James", "Giannis", "Luka", "Jokic", "Embiid", "Tatum", "Unknown_Rookie"],
    "Team": ["Lakers", "Warriors", "Suns", "Lakers", "Bucks", "Mavs", "Nuggets", "Sixers", "Celtics", "Jazz"],
    "Points": [28.9, 29.4, 29.1, 28.9, 31.1, 32.4, 24.5, 33.1, 30.1, 5.0],
    "Salary": [47000000, 48000000, 44000000, 47000000, 42000000, 37000000, None, 35000000, 30000000, 1000000]
}

df = pd.DataFrame(raw_data)
df.to_csv("nba_raw_data.csv", index=False)
print("✅ Source file 'nba_raw_data.csv' has been created.")
