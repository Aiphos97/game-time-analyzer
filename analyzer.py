import pandas as pd

# Load your CSV
df = pd.read_csv('game.csv')

# Show the first few rows to confirm it loaded correctly
print("🎮 Your Game Log:")
print(df.head())

# Total time played
total_time = df['Duration (mins)'].sum()
print(f"\n⏱️ Total time played: {total_time} minutes")

# Time played per game
print("\n🕹️ Time played per game:")
print(df.groupby('Game')['Duration (mins)'].sum().sort_values(ascending=False))

# Optional: Time per platform
print("\n💻 Time played per platform:")
print(df.groupby('Platform')['Duration (mins)'].sum())