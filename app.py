from flask import Flask, render_template, request, url_for
from datetime import datetime
import json

app = Flask(__name__)
submitted_names = []

@app.route('/')
def home():
    day = datetime.today().strftime('%A')
    print(day)
    return render_template('index.html', day=day, current_time=datetime.now().strftime('%H:%M:%S'))

@app.route('/second/<name>')
def second(name):
    print(name)
    return "Hi " + name + ", Welcome to my Second Page!, hello world"

@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        submitted_data = request.form.to_dict()
        name = submitted_data.get('name')
        if name:
            submitted_names.append(name)
    else:
        submitted_data = request.args.to_dict()
        name = submitted_data.get('name')

    info_json = json.dumps(submitted_data, indent=2)
    return render_template('info.html', name=name, info_json=info_json)

@app.route('/history')
def history():
    return render_template('history.html', names=submitted_names)

if __name__ == '__main__':
    app.run(debug=True)