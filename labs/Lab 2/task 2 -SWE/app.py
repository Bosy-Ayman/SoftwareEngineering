from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    email = None
    name = None
    phone = None

    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        phone = request.form.get('phone')

    return render_template('script.html',email=email, name=name, phone=phone)  

if __name__ == '__main__':
    app.run(debug=True, port=3001)
