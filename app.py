from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fihing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Fish(db.Moel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

app.app_context().push()
def __repr__(self):
    return '<Fish %r>' %self.id

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/journeys')
def journeys():
    return render_template('journeys.html')

@app.route('/places')
def places():
    return render_template('places.html')

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'user page' + name + "-" + str(id)

if __name__=='__main__':
    app.run(debug=True)