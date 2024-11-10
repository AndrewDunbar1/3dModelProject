from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Set up Flask and allow CORS to accept requests from the web page
app = Flask(__name__)
CORS(app)

# Set up OpenAI API key
openai.api_key = 'asdf'

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    user_input = data.get("user_input")
    print(f"Received user input: {user_input}")  # Debugging: log user input

    # OpenAI prompt to make it more structured
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that translates user instructions into commands like 'rotate left', 'rotate right', 'move up', 'move down', 'move forward', or 'move backward' to control a 3D model."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=50
    )

    # Extracting response from OpenAI
    command = response.choices[0].message['content'].strip().lower()
    print(f"Command from OpenAI: {command}")  # Debugging: log the command
    return jsonify({"command": command})


if __name__ == '__main__':
    app.run(port=5000)