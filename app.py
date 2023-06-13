from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/journeys')
def journeys():
    return render_template('journeys.html')

@app.route('/places')
def places():
    return render_template('places.html')


if __name__=='__main__':
    app.run(debug=True)