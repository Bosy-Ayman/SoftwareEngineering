from flask import Flask ,render_template
app= Flask(__name__)

@app.route('/')
def home():
  return 'hello docker file'

@app.route('/information')
def information():
  return 'what is Docker'


if __name__ == '__main__':
  app.run(host='0.0.0.0',port = 4000,debug=True)
