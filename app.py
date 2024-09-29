from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Função para carregar o arquivo XLSX com credenciais
def load_credentials():
    df = pd.read_excel('credencials.xlsx')
    return df

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Carrega o arquivo XLSX
    credentials = load_credentials()

    # Verifica se existe a combinação de usuário e senha
    user = credentials[(credentials['username'] == username) & (credentials['password'] == password)]
    
    if not user.empty:
        report_link = user.iloc[0]['reportLink']
        return jsonify({'status': 'success', 'reportLink': report_link})
    else:
        return jsonify({'status': 'error', 'message': 'Credenciais incorretas!'}), 401

if __name__ == '__main__':
    app.run(debug=True)
