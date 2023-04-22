from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    if query.lower() == 'google':
        return redirect('https://www.google.com')
    else:
        return 'Pesquisa não suportada'

if __name__ == '__main__':
    app.run()
