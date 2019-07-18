from flask import Flask, render_template
from lasttest import mainfunc

app = Flask(__name__)


  

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/my-link/')
def background_process_test():
    mainfunc()
    print ("hello")
    return ()



if __name__ == '__main__':
  app.run(debug=True)
  