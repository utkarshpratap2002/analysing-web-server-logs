import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Defining the column names/ regex
col_names = ['saddr', 'daddr', 'proto', 'sport', 'dport', 'state', 'stos', 'dtos', 'swin', 'dwin', 'shops', 'dhops', 'stime', 'ltime', 'sttl', 'dttl', 'tcprtt', 'synack', 'ackdat', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'sappbytes', 'dappbytes', 'dur', 'pkts', 'bytes', 'appbytes', 'rate', 'srate', 'drate', 'label']

# Read and Parse the 
df = pd.read_csv('capture20110810.binetflow.2format.txt', header=1, engine='python', names=col_names)

# Load the data AGAIN to have a fresh copy with the original strings
df_original = pd.read_csv('capture20110810.binetflow.2format.txt', header=1, engine='python', names=col_names)

# In your main dataframe, perform the coercion
df['sport'] = pd.to_numeric(df['sport'],errors="coerce")

# Now, find the index of the problematic rows from your main df
problematic_indices = df[df['sport'].isnull()].index

# Using problematic_indices to see what values are coming on these indices
original_problem_values = df_original.loc[problematic_indices]


# Printing the sample values
print("Printing the Sample Values for Problematic Values from the Original Data: ")
print(original_problem_values[["proto", "sport", "dport", "label"]].head(20))

print("\nWhat are the unique non-numeric 'sport' values?")
print(original_problem_values["sport"].value_counts())
