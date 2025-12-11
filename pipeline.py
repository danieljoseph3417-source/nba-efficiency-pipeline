import pandas as pd

#1. EXTRACT
print(f"Extracting data...")
df = pd.read_csv("nba_raw_data.csv")

#2. CLEAN
print(f"Cleaning data...")
df = df.drop_duplicates()
df = df.dropna()

#3. TRANSFORM
print(f"Transforming data...")
df['Cost_Per_Point'] = df['Salary'] / df['Points']

#4. ANALYZE
print(f"Analyzing efficiency...")
team_analysis = df.groupby('Team')['Cost_Per_Point'].mean().reset_index()
clean_team_analysis = round(team_analysis, 2)

#5. LOAD
print(f"Saving report...")
clean_team_analysis.to_csv("nba_report.csv", index=False)
print(f"✅ Pipeline finished successfully! .")