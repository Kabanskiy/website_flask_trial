from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fihing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

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
    fishes = Fish.query.order_by(Fish.data).all()
    return render_template('places.html', fishes=fishes)

@app.route('/create-place', methods=['POST', 'GET'])
def create_place():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        fish = Fish(title=title, intro=intro, text=text)

        try:
            db.session.add(fish)
            db.session.commit()
            return redirect('/home')
        except:
            return 'Что-то пошло не так...'
    else:
        return render_template('create-place.html')


if __name__=='__main__':
    app.run(debug=True)