from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "homepage"

@app.route('/about')
def about():
    return "Website about content here!"

if __name__=='__main__':
    app.run(debug=True)