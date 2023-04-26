from flask_frozen import Freezer

# Define o objeto do aplicativo Flask
app = Flask(__name__)

# Define o objeto do Freezer
freezer = Freezer(app)

# Define uma rota para o seu aplicativo Flask
@app.route('/')
def index():
    resultado = "Este é o meu resultado!"
    return render_template('resultado.html', resultado=resultado)

# Gera as páginas HTML estáticas do seu aplicativo Flask
if __name__ == '__main__':
    freezer.freeze()
