from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///flask.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False)
    uemail = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(20), default = '123')

    def __repr__(self):
        return '<User %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        uname = request.form['username']
        uemail = request.form['uemail']
        password = request.form['upassword']

        create_user_record = User(name = uname, uemail=uemail , password= password)
        try:
            db.session.add(create_user_record)
            db.session.commit()
        except:
            return "Error happened"

        return redirect('/dashboard')
    else:
        return render_template('index.html')

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    users = User.query.all()
    return render_template('dashboard.html', users=users)



if __name__ == "__main__":
    app.run(port='8098', debug=True)
