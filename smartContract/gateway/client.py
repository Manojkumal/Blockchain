# client.py
import requests

BASE_URL = "http://127.0.0.1:8080"

# Deposit
resp = requests.post(f"{BASE_URL}/deposit", json={"account_id":"user1","value":100})
print(resp.json())

# Query
resp = requests.get(f"{BASE_URL}/query/user1")
print(resp.json())

# Withdraw
resp = requests.post(f"{BASE_URL}/withdraw", json={"account_id":"user1","value":30})
print(resp.json())

#Query
resp1 = requests.get(f"{BASE_URL}/query/user1")
print(resp1.json())


# Set Policy
resp = requests.post(f"{BASE_URL}/set_policy", json={"account_id":"user1","policy":"active"})
print(resp.json())

# Get Policy
resp = requests.get(f"{BASE_URL}/get_policy/user1")
print(resp.json())
