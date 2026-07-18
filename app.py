from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = "tasks_data.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

@app.route('/')
def index():
    my_tasks = load_tasks()
    return render_template('index.html', tasks=my_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task_text', '').strip()
    if task_text:
        my_tasks = load_tasks()
        my_tasks.append(task_text)
        save_tasks(my_tasks)
    return redirect(url_for('index'))

@app.route('/remove/<int:task_index>', methods=['POST'])
def remove_task(task_index):
    my_tasks = load_tasks()
    if 0 <= task_index < len(my_tasks):
        my_tasks.pop(task_index)
        save_tasks(my_tasks)
    return redirect(url_for('index'))

@app.route('/exit', methods=['POST'])
def exit_server():
    import os
    import signal
    os.kill(os.getpid(), signal.SIGINT)
    return "<h3>Server safely terminated. You can close this tab now!</h3>"

if __name__ == '__main__':
    app.run(debug=True)