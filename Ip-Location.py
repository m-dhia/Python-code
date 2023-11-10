import requests

## Single ip request ###

# response = requests.get("http://ip-api.com/json/24.48.0.1").json()
# print(response['lat'])
# print(response['lon'])

### Batch ip request ###

response = requests.post(" http://ip-api.com/batch", json=[
    {"query": "208.80.152.201"},
    {"query": "167.72.3.52"},
    {"query": "157.230.75.212"},
    {"query": "157.230.57.212"}

]).json()

# Iterate through the responses for each IP address in the batch
for ip_info in response:
    # Iterate through the key-value pairs in the IP information
    for k,v in ip_info.items():
        print(k,v)
    # Print a newline for better readability between IP information    
    print("\n")