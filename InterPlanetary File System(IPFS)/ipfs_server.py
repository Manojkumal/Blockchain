#!/usr/bin/env python3

from flask import Flask, request, jsonify, send_file
from RPC_ipfs import RPC_Curl
import tempfile
import os
import json

app = Flask(__name__)

# IPFS RPC port (mapped from Docker)
IPFS_RPC_PORT = 5001
rpc = RPC_Curl(IPFS_RPC_PORT)


@app.route("/ipfs/add", methods=["POST"])
def add_file():
    """
    Upload a file to IPFS
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        file.save(tmp.name)
        tmp_path = tmp.name

    try:
        result = rpc.save_file(tmp_path)
        ipfs_response = json.loads(result['results'])
        return jsonify(ipfs_response)
    finally:
        os.remove(tmp_path)


@app.route("/ipfs/cat/<string:cid>", methods=["GET"])
def cat_file(cid):
    """
    Retrieve file content from IPFS by CID
    """
    result = rpc.retrive_file(cid)

    if result['status'] != 200:
        return jsonify({"error": "Failed to retrieve file"}), 500

    # Return raw bytes
    return result['results']


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
