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

@app.route('/places')
def places():
    return render_template('places.html')

@app.route('/journeys')
def journeys():
    fishes = Fish.query.order_by(Fish.date.desc()).all()
    return render_template('journeys.html', fishes=fishes)

@app.route('/journeys/<int:id>')
def journey_read(id):
    fish = Fish.query.get(id)
    return render_template('journey_read.html', fish=fish)

@app.route('/journeys/<int:id>/delete')
def journey_delete(id):
    fish = Fish.query.get_or_404(id)

    try:
        db.session.delete(fish)
        db.session.commit()
        return redirect('/journeys')
    except:
        return 'Что-то пошло не так...'


@app.route('/journeys/<int:id>/update', methods=['POST', 'GET'])
def journey_update(id):
    fish = Fish.query.get(id)
    if request.method == 'POST':
        fish.title = request.form['title']
        fish.intro = request.form['intro']
        fish.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/journeys')
        except:
            return 'Что-то пошло не так...'
    else:
        fish = Fish.query.get(id)
        return render_template('journey_update.html', fish=fish)

@app.route('/create-journey', methods=['POST', 'GET'])
def create_journey():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        fish = Fish(title=title, intro=intro, text=text)

        try:
            db.session.add(fish)
            db.session.commit()
            return redirect('/journeys')
        except:
            return 'Что-то пошло не так...'
    else:
        return render_template('create-journey.html')


if __name__=='__main__':
    app.run(debug=True)