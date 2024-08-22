from flask import Flask, render_template, request, redirect
from database import db, init_db, Users
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_test.db"
init_db(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['pass']
        users = Users(name=name, email=email, password=password)
        db.session.add(users)
        db.session.commit()
    show = Users.query.all()
    return render_template('index.html', users=show)

@app.route('/show', methods=['GET', 'POST'])
def show_users():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['pass']
        users = Users(name=name, email=email, password=password)
        db.session.add(users)
        db.session.commit()
    show = Users.query.all()
    return render_template('index.html', users=show)

@app.route('/delete/<int:id>')
def delete(id):
    user = Users.query.filter_by(uid=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    user = Users.query.filter_by(uid=id).first()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['pass']
        user.name = name
        user.email = email
        user.password = password
        db.session.add(user)
        db.session.commit()
        return redirect('/')

    return render_template('update.jinja', user=user)

if __name__ == "__main__":
	app.run(debug=True, port=5000)


# Install Flask-Migrate: pip install Flask-Migrate
# Initialize migrations: flask db init
# Create a migration: flask db migrate -m "Initial migration."
# Apply the migration: flask db upgrade