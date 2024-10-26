from flask import Flask, request, jsonify
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner3 import clean_corpus  # Ensure this script is correctly implemented
import os

# Path to the educational data file
CORPUS_FILE = "edu_chat.txt"

# Create the chatbot instance
chatbot = ChatBot(
    "EduBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",  # For math-related queries
        "chatterbot.logic.TimeLogicAdapter"         # For time-related responses
    ]
)

# Train the chatbot with the educational corpus
if os.path.exists(CORPUS_FILE):
    trainer = ListTrainer(chatbot)
    cleaned_corpus = clean_corpus(CORPUS_FILE)  # Ensure this function returns cleaned lines of text
    trainer.train(cleaned_corpus)
else:
    print(f"Corpus file '{CORPUS_FILE}' not found. Please ensure it exists.")

# Function to get chatbot response
def get_bot_response(user_input):
    return str(chatbot.get_response(user_input))

# Flask app setup
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests

@app.route('/get_response', methods=['POST'])
def get_response():
    # Get the user input from the request
    user_message = request.json.get('message', '')
    
    # Get chatbot response
    response = get_bot_response(user_message)
    
    # Send the response back to the frontend
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
