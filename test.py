from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('welcome', name=name))
    return render_template('index.html')

@app.route('/welcome/<name>')
def welcome(name):
    message = f'Welcome {name}!'
    return render_template('welcome.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)