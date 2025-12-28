# %% [markdown]
# Data Preprocessing

# %% [markdown]
# Import the libraries

# %%
import pandas as pd

# %% [markdown]
# Load the dataset

# %%
df = pd.read_csv("microsoft.csv")

# %% [markdown]
# Preview the dataset

# %%
print(df.head())
print(df.info())

# %% [markdown]
# Convert the "Date" column to datetime objects

# %%
df["Date"] = pd.to_datetime(df["Date"])

# %% [markdown]
# Print the information to confirm the data type has changed

# %%
print(df.info())

# %% [markdown]
# Handling missing values

# %%
df_missing = df.isnull().sum()
print(df_missing)

# %% [markdown]
# Handling Duplicates

# %%
df_duplicated = df.duplicated().sum()
print(df_duplicated)

# %% [markdown]
# Feature Engineering

# %%
# Create new feature from the "Date" column
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Day_of_Week"] = df["Date"].dt.dayofweek

# %% [markdown]
# Set the Date Column as the Index

# %%
df.set_index("Date",inplace=True)

# %% [markdown]
# Rename the Column for Clarity

# %%
df.rename(columns={
    "Close": "close",
    "High": "high",
    "Low": "low",
    "Open": "open",
    "Volume": "volume",
    "Year": "year",
    "Month": "month",
    "Month":"month",
    "Day": "day",
    "Day_of_Week": "day_of_week"
},inplace=True)

# %% [markdown]
# Display the first 5 rows and the information

# %%
print(df.head())
print(df.info())

# %% [markdown]
# Saved the cleaned data

# %%
df.to_csv("microsoftcleaned.csv",index=True)
print("Saved Successfully")


