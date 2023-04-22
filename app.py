from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def get_text():
    if request.method == 'POST':
        text = request.form['text']
        if text.lower() == 'google':
            return redirect('https://www.google.com')
        else:
            return 'Texto não suportado'


if __name__ == '__main__':
    app.run()
