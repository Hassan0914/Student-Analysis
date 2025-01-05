import pandas as pd

# Load the original CSV file
df = pd.read_csv('Global Health Statistics.csv')

# Randomly sample 50% of the data (without replacement)
df_sampled = df.sample(frac=0.1,random_state=1)

# Save the sampled data to a new CSV file
df_sampled.to_csv('Global Health Statistics Sampled.csv', index=False)

print("50% of the data has been deleted, and the new file is saved.")
