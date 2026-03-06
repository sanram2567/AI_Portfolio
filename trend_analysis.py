import pandas as pd

# 1. Load your AI-generated data
df = pd.read_csv('analysis_log.csv')

# 2. Count the frequency of each caption
trend = df['AI Caption'].value_counts()

print("--- AI VISION TREND REPORT ---")
print(trend)