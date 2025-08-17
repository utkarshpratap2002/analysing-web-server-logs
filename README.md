# Web Server Log Analyzer

This project provides a Python script to analyze web server logs, extracting key information, identifying patterns, and pinpointing potential issues or suspicious activities. It leverages the power of the Pandas library for data manipulation and analysis, along with regular expressions (re) for robust log parsing and Matplotlib and Seaborn for data visualization.

# Features
- Log Parsing: Uses regular expressions to extract relevant fields from web server log entries (e.g., IP address, timestamp, request method, URL, status code, response size).
- Data Transformation: Converts parsed data into a structured Pandas DataFrame for efficient analysis.
- Timestamp Conversion: Transforms raw timestamp strings into datetime objects for time-based analysis.
- Error Analysis: Identifies and quantifies HTTP status code distribution, particularly focusing on client-side errors (4xx codes).
- Suspicious IP Detection: Highlights client IP addresses associated with a high number of client-side errors, potentially indicating malicious activity.
- Visualization: Provides a pie chart to visually represent the distribution of HTTP status codes.

# Getting started

Prerequisites: 
- `Python 3.x`
- Pandas library (`pip install pandas`)
- Matplotlib library (`pip install matplotlib`)
- Seaborn library (`pip install seaborn`)

Installation:
- Clone this repository: `git clone https://github.com/utkarshpratap2002/analysing-web-server-logs.git`
- Navigate to the project directory: `cd analysing-web-server-logs` 

Usage: 
- Place your web server log file (e.g., access.log) in the project directory.
- Run the Python script: `python log_analyzer.py` (Note: Replace log_analyzer.py with the actual name of your script).
- The script will generate output showing the cleaned DataFrame information, HTTP status code distribution, and a list of IP addresses with the most client-side errors. It will also display a pie chart visualizing the status code distribution. 

Customization: 
- Log file name: Modify the with open('access.log', 'w') as f: line in the code to use your specific log file name.
- Log format (`regex`): If your web server logs follow a different format, you'll need to adjust the `log_regex` variable to match the structure of your log entries. 


# Output

```
Cleaned DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype              
---  ------         --------------  -----              
 0   ip_address     9 non-null      object             
 1   timestamp      9 non-null      datetime64[ns, UTC]
 2   status_code    9 non-null      int64              
 3   response_size  9 non-null      int64              
 4   method         9 non-null      object             
 5   url            9 non-null      object             
dtypes: datetime64[ns, UTC](1), int64(2), object(3)
memory usage: 560.0+ bytes

Status Code Distribution:
200    5
404    3
403    1
Name: status_code, dtype: int64

IPs with the most client-side errors (4xx):
10.0.0.5      3
203.0.113.45    1
Name: ip_address, dtype: int64
```