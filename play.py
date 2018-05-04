from flask import Flask, render_template
app = Flask(__name__)


print (__name__)
@app.route('/')

def hell0_world():
    return 'Hello World!'

@app.route('/play/<int:x>/<string:color>')
def playground(x,color):
    return render_template('index.html', x = x, color = color)
if __name__=="__main__":
    app.run(debug=True)
