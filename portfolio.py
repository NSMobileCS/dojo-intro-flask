from flask import Flask, render_template  
app = Flask(__name__)

@app.route('/')
def indexpage():
    return render_template('welcome.html')

@app.route('/about')
def abtpage():
    return render_template('about.html')

@app.route('/projects')
def projpage():
    return render_template('projects.html')

app.run(debug=True)