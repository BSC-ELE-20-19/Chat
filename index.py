import os
from flask import Flask, Response, request
from chatbot import sending

app = Flask(__name__)

#TODO: create incoming messages route
@app.route('/')
def index():
    return "Welcome to Offline AI Farmer!"
@app.route('/incoming', methods=['POST', 'GET'])
def incoming_messages():
    try:
        message = request.form.get('text')
        phone_number = request.form.get('from')
        print(f"Received message: '{message}' from {phone_number}")
        sending(message, phone_number)
        return "OK", 200
    except Exception as e:
        print("Error:", e)
        return "Bad Request", 400

#TODO: create delivery reports route.
if __name__ == "__main__":
    app.run(debug=True, port = os.environ.get("PORT", 5000))
