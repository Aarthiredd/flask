from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('loginp.html')
     
@app.route('/login', methods=['POST'])

class logina:
{  def __init__(aa, username, password):
    aa.username = username
    aa.password = password

a1 = logina("abcd","efgh")

print(a1.username)
print(a1.password)

if()
if __name__ == '__main__':
   app.run()