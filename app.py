from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Executa seu script Python aqui e armazena o resultado em uma variável
    resultado = """
<!DOCTYPE html>
<html>
<head>
    <title>Resultado</title>
</head>
<body>
    <h1>Resultado:</h1>
    <p>{{ resultado }}</p>
</body>
</html>

"""
    
    # Renderiza o resultado usando um template HTML
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run()
