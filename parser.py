import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# For plotting the data
sns.set_style("whitegrid")

# Defining the column names/ regex
col_names = ['saddr', 'daddr', 'proto', 'sport', 'dport', 'state', 'stos', 'dtos', 'swin', 'dwin', 'shops', 'dhops', 'stime', 'ltime', 'sttl', 'dttl', 'tcprtt', 'synack', 'ackdat', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'sappbytes', 'dappbytes', 'dur', 'pkts', 'bytes', 'appbytes', 'rate', 'srate', 'drate', 'label']

# Loading the Data into the Schema
try: 
    df = pd.read_csv('capture20110810.binetflow.2format.txt', header=1, engine='python', names=col_names)
    print("Data Loaded Successfully!")
except FileNotFoundError:
    print("Error: The data file was not found. Please make sure 'capture20110810.binetflow.2format.txt' is in the same directory.") 
    exit()

print(f"Initial DataFrame Shape: {len(df)}")

# Goal 
# - Filter all the traffic that is coming from botnet
# - Find out which services botnet is talking to & analyse how frequent the process is
#   - Find out counts for each service 
#   - Find out what else is being send/recieve
# - Check when was the botnet active


# Data Cleaning and Processing
print("Cleaning the data ... ")


# 1. Decision on ICMP/ARP Traffic: Filter for TCP and UDP only
filtered_tcp_udp = df[df['proto'].isin(['tcp', 'udp'])].copy()
print(f"Filtered for TCP/UDP only. Kept {len(filtered_tcp_udp.index)} rows out of {len(df)}.")

# 2. Convert port columns to numeric type. Now it will work without errors.
filtered_tcp_udp['sport'] = filtered_tcp_udp['sport'].astype(int)
filtered_tcp_udp['dport'] = filtered_tcp_udp['dport'].astype(int)

# 3. Create the ground truth 'is_botnet' column
botnet_ip = '147.32.84.165'
filtered_tcp_udp['is_botnet'] = (filtered_tcp_udp['saddr'] == botnet_ip).astype(int)
print("\n`is_botnet` column created. Distribution: ")
print(filtered_tcp_udp['is_botnet'].value_counts())






