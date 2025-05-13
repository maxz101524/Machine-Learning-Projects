import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Read the dataset
print("Reading the dataset...")
df = pd.read_csv('IS304_FinalProject/openpowerlifting.csv')

# Split into male and female datasets
print("Splitting into male and female datasets...")
df = df[df['Equipment'] == 'Raw']
df = df[df['BodyweightKg'] != '']
df = df[df['Event'] == 'SBD']
male_df = df[df['Sex'] == 'M']
female_df = df[df['Sex'] == 'F']

# Take random samples
print("Taking random samples...")
male_sample = male_df.sample(n=5000, random_state=42)
female_sample = female_df.sample(n=5000, random_state=42)

# Combine the samples
print("Combining samples...")
sampled_df = pd.concat([male_sample, female_sample])

# Save to new CSV
print("Saving to new CSV...")
sampled_df.to_csv('IS304_FinalProject/openpowerlifting_sampled.csv', index=False)

print("Done! New dataset saved as 'openpowerlifting_sampled.csv'")
print(f"Total entries in new dataset: {len(sampled_df)}")
print(f"Male entries: {len(male_sample)}")
print(f"Female entries: {len(female_sample)}") 