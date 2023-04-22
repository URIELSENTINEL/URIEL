from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ARTHUR')
def funcao():
    # Aqui você pode definir sua função em Python
    return "Essa é uma função em Python"

if __name__ == '__main__':
    app.run(debug=True)
