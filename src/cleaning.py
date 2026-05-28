import pandas as pd

df = pd.read_csv("raw_data.csv")
df["post"] = df["post"].str.lower().str.strip()
df.to_csv("cleaned_data.csv", index=False)

print("cleaning completed")
