# server.py

from flask import Flask, request, jsonify
import sys
sys.path.append("../middleware")
import middleware

app = Flask(__name__)

# Deposit
@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    account_id = data['account_id']
    value = int(data['value'])
    result = middleware.deposit(account_id, value)
    return jsonify({"result": result})

# Withdraw
@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    account_id = data['account_id']
    value = int(data['value'])
    result = middleware.withdraw(account_id, value)
    return jsonify({"result": result})

# Query
@app.route('/query/<account_id>', methods=['GET'])
def query(account_id):
    balance = middleware.query(account_id)
    return jsonify({"balance": balance})

# Set Policy
@app.route('/set_policy', methods=['POST'])
def set_policy():
    data = request.get_json()
    account_id = data['account_id']
    policy = data['policy']
    result = middleware.set_policy(account_id, policy)
    return jsonify({"result": result})

# Get Policy
@app.route('/get_policy/<account_id>', methods=['GET'])
def get_policy(account_id):
    policy = middleware.get_policy(account_id)
    return jsonify({"policy": policy})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

