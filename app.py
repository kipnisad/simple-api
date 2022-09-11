# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/myip")
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.get("/myrealip")
def get_my_real_ip():
    return jsonify({'real_ip': request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   }), 200

app.run(debug=True, host='0.0.0.0', port = 5000)