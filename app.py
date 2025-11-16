from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Página inicial

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')  # Página sobre

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')  # Página galeria

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')  # Página contatos

@app.route('/cultura')
def cultura():
    return render_template('cultura.html')  # Página cultura

@app.route('/tecnologia')
def tecnologia():
    return render_template('tecnologia.html')  # Página tecnologia

if __name__ == '__main__':
    app.run(debug=True)
