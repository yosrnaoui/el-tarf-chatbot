from flask import Flask, request, jsonify
from chatbot_logic import process_query

app = Flask(__name__)

@app.route("/")
def home():
    return "🌍 Welcome to the El Tarf chatbot!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("message", "")
    response = process_query(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
