from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    template = """
    <!doctype html>
    <html>
      <head>
        <title>{{ title }}</title>
      </head>
      <body>
        <h1>{{ header }}</h1>
      </body>
    </html>
    """
    return render_template_string(template, title='URIEL SENTINEL', header='URIEL')

if __name__ == '__main__':
    app.run()
