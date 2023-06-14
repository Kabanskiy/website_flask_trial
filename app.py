from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
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

# @app.route('/user/<string:name>/<int:id>')
# def user(name, id):
#     return 'user page' + name + "-" + str(id)

if __name__=='__main__':
    app.run(debug=True)