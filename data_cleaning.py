import pandas as pd

import pandas as pd

df = pd.read_excel("dataset.csv")

print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
for col in df.select_dtypes(include="number"):
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include="object"):
    df[col] = df[col].fillna("Unknown")

# Standardize text columns
for col in df.select_dtypes(include="object"):
    df[col] = df[col].astype(str).str.strip().str.title()

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)
df.to_excel("cleaned_dataset.xlsx", index=False)

print("Cleaning Completed Successfully!")
