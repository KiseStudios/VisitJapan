from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')  # Serve index.html diretamente

# Rota para a página sobre
@app.route('/sobre')
def sobre():
    return send_from_directory(os.getcwd(), 'sobre.html')  # Serve sobre.html diretamente

# Rota para a página galeria
@app.route('/galeria')
def galeria():
    return send_from_directory(os.getcwd(), 'galeria.html')  # Serve galeria.html diretamente

# Rota para a página de contatos
@app.route('/contatos')
def contatos():
    return send_from_directory(os.getcwd(), 'contatos.html')  # Serve contatos.html diretamente

# Rota para a página cultura
@app.route('/cultura')
def cultura():
    return send_from_directory(os.getcwd(), 'cultura.html')  # Serve cultura.html diretamente

# Rota para a página de tecnologia
@app.route('/tecnologia')
def tecnologia():
    return send_from_directory(os.getcwd(), 'tecnologia.html')  # Serve tecnologia.html diretamente

if __name__ == '__main__':
    app.run(debug=True)
