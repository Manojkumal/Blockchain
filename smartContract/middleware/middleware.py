# middleware.py

from web3 import Web3
import json

# Connect to local Ethereum node (Ganache)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if not w3.isConnected():
    raise Exception("Failed to connect to Ethereum node")

# Load deployed contract ABI
with open("../build/contracts/TokenManager.json") as f:
    contract_json = json.load(f)
    contract_abi = contract_json['abi']

# Deployed contract address (replace with your actual deployed address)
raw_address = "0xe23fbbd831242aeF422C853da61A6f9A7179Ebf6"
contract_address = w3.toChecksumAddress(raw_address)
# Connect to contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Use first account from Ganache as sender
account = w3.eth.accounts[0]

# --------------------------
# Transact functions (write to blockchain)
# --------------------------

def deposit(account_id, value):
    tx = contract.functions.Deposit(account_id, value).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx)
    return f"Deposited {value} tokens to {account_id}"

def withdraw(account_id, value):
    tx = contract.functions.Withdraw(account_id, value).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx)
    return f"Withdrew {value} tokens from {account_id}"

def set_policy(account_id, policy):
    tx = contract.functions.Set_Policy(account_id, policy).transact({'from': account})
    w3.eth.wait_for_transaction_receipt(tx)
    return f"Policy set for {account_id} as '{policy}'"

# --------------------------
# Call functions (read from blockchain)
# --------------------------

def query(account_id):
    return contract.functions.Query(account_id).call()

def get_policy(account_id):
    return contract.functions.Get_Policy(account_id).call()

