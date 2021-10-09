from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()   