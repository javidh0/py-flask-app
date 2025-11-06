from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define a single route
@app.route('/')
def home():
    return "👋 Welcome to my Python Flask server!"

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1729, debug=True)
