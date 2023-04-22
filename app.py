from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ARTHUR', methods=['GET', 'POST'])
def funcao():
    # Aqui você pode definir sua função em Python
    response = make_response("Essa é uma função em Python")
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)
