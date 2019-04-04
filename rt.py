from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def render():
    return render_template('loginp.html')
     
@app.route('/login', methods=['POST'])
def login():
    return ("Hello " + request.form['username'] + " Welcome to NeonMob!!")

if __name__ == '__main__':
   app.run()


