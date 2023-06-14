from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "hello Uassya"
    # return render_template('home.html')

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