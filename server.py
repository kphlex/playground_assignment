from flask import Flask, render_template


app = Flask(__name__)


@app.route('/play')
def first_chall():
    return render_template('index.html', count=3, color="blue")



@app.route('/play/<int:count>')
def second_chall(count):
    return render_template('index.html', count=count, color="blue")



@app.route('/play/<int:count>/<string:color>')
def third_chall(count, color):
    return render_template('index.html', count=count, color=color)



if __name__=='__main__':
    
    app.run(debug=True)