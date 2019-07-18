from flask import Flask, render_template

from .lasttest import mainfunc

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  mainfunc()
  print ('I got clicked!')

  return 'Script is running'

if __name__ == '__main__':
  app.run(debug=True)