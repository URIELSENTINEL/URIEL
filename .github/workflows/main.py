from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def URIEL():
    return render_template('URIEL.html')

if __name__ == '__main__':
    app.run()
