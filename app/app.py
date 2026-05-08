from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    # return "render_template('index.html')"
    return "Hello, World! This is a Flask application running in a Docker container."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)