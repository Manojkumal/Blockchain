import requests

SERVER_URL = "http://127.0.0.1:8000"

# -------- Upload file --------
files = {
    "file": open("test_file.txt", "rb")
}

resp = requests.post(f"{SERVER_URL}/ipfs/add", files=files)
resp.raise_for_status()

data = resp.json()
cid = data["Hash"]
print("Uploaded CID:", cid)

# -------- Download file --------
resp = requests.get(f"{SERVER_URL}/ipfs/cat/{cid}")
resp.raise_for_status()

with open("downloaded_test_file.txt", "wb") as f:
    f.write(resp.content)

print("File downloaded successfully")
