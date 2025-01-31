from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []  

def get_tasks():
    return tasks

def add_task(task):
    tasks.append(task)

@app.route('/')
def index():
    return render_template('index.html', tasks=get_tasks())

@app.route('/add-task', methods=['POST'])
def add_task_route():
    task = request.form.get('task') 
    if task:
        add_task(task)  
    return redirect('/')  

if __name__ == '__main__':
    app.run(debug=True)
