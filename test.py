from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('loginp'))
    return render_template('loginp.html', error=error)

if __name__ == '__main__':
    app.run()