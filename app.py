from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('templates/index.html')

@app.route('/URIEL/ARTHUR/')
def funcao():
    return render_template('templates/repositorio/arthur.html')

if __name__ == '__main__':
    app.run(debug=True)
