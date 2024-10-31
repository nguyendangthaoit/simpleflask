from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure App Service Release!"

if __name__ == '__main__':
    app.run(debug=True)
