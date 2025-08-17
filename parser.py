import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Define column names and a regex to parse the log file
log_regex = r'([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+)'
column_names = ['ip_address', 'timestamp', 'request', 'status_code', 'response_size']

# Read and parse the log file
df = pd.read_csv('access.log', sep=log_regex, engine='python', header=None, names=['extra'] + column_names + ['extra2'])
df = df.drop(columns=['extra', 'extra2'])
# print(df.head())

# Transforming the data

df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%b/%Y:%H:%M:%S %z')

# Convert status_code and response_size to numeric types
df['status_code'] = pd.to_numeric(df['status_code'])
df['response_size'] = pd.to_numeric(df['response_size'])

# Extract request method, URL, and protocol
request_parts = df['request'].str.split(' ', n=2, expand=True)
df['method'] = request_parts[0]
df['url'] = request_parts[1]
df['protocol'] = request_parts[2]

# Drop the original request column
df = df.drop(columns=['request'])

print("\nCleaned DataFrame Info:")
df.info()
# print(df.head())

# Status code distribution
status_counts = df['status_code'].value_counts()
print("\nStatus Code Distribution:")
print(status_counts)

# Visualize it
plt.figure(figsize=(8, 8))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('HTTP Status Code Distribution')
# plt.show()

# Find IPs that generate a lot of client errors (4xx status codes)
error_df = df[df['status_code'] >= 400]
suspicious_ips = error_df['ip_address'].value_counts()

print("\nIPs with the most client-side errors (4xx):")
print(suspicious_ips)



