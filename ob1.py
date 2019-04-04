from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def render():
    return render_template('loginp.html', )
     
@app.route('/login', methods=['GET','POST'])

def user_info():
    
    if request.method =='POST':
        obj={'username':'aarthi.reddy','password':'welcomeback1'}
        if request.form['username']== obj['username'] or request.form['password']== obj['password']:
            message = "SUCCESSFULLY LOGGED IN"
        else:
            message = "ERROR! PLEASE TRY AGAIN."
            

if __name__ == '__main__':
   app.run()