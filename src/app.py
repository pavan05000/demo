from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/health')
def health():
    app.logger.info("Health check called.")
    return "Now you're viewing Health page", 200

@app.route('/')
def home():
    app.logger.info("Home page hit!")
    return "Welcome to the Sample App!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

