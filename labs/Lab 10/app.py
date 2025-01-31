from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
tasks = []

def add_task(task):
    if task not in tasks: 
        print(f"Adding task: {task}") 
        tasks.append(task)

def get_tasks():
    return tasks

@app.route('/')
def home():
    return render_template('index.html', tasks=get_tasks())

@app.route('/add_task', methods=['POST']) 
def add_tasks():
    task = request.form['task']
    add_task(task)
    return redirect('/')  

if __name__ == '__main__':
    app.run(debug=True)
