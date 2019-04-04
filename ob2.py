from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/success/<name>')

def render():
    return render_template('loginp.html')

def success(username):
   return 'welcome %s' % username

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',username = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',username = user))

if __name__ == '__main__':
   app.run(debug = True)