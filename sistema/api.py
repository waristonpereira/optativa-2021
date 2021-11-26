from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

from controladores.controlador_usuario import ControladorUsuario

app = Flask(__name__)
run_with_ngrok(app)

controladorUsuario = ControladorUsuario()

@app.route("/usuario", methods=["POST"])
def cadastrar_usuario():
    try:
        dados = request.get_json()
        usuario = dados["usuario"]
        senha = dados["senha"]
        controladorUsuario.cadastrar_usuario(usuario, senha)
        return {"status": "OK", "mensagem": "Cadastrado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar"}

@app.route("/usuario/<id>", methods=["PUT"])
def atualizar_usuario(id):
    try:
        dados = request.get_json()
        usuario = dados["usuario"]
        senha = dados["senha"]
        controladorUsuario.atualizar_usuario(id, usuario, senha)
        return {"status": "OK", "mensagem": "Atualizado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao atualizar"}

@app.route("/usuario/<id>", methods=["DELETE"])
def excluir_usuario(id):
    try:
        controladorUsuario.excluir_usuario(id)
        return {"status": "OK", "mensagem": "Excluído com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao excluir"}

@app.route("/login", methods=["POST"])
def verificar_usuario_senha():
    try:
        dados = request.get_json()
        usuario = dados["usuario"]
        senha = dados["senha"]
        if controladorUsuario.verificar_usuario_senha(usuario, senha):
            return {"status": "OK", "mensagem": "Acesso OK!"}
        else:
            return {"status": "ERRO", "mensagem": "Usuário/Senha Inválidos!"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao efetuar o login"}

@app.route("/usuario")
def listar_todos():
    try:
        todos = controladorUsuario.buscar_todos_usuarios()
        return jsonify(todos)
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter usuarios"}

@app.route("/usuario/<id>")
def listar_usuario(id):
    try:
        usuario = controladorUsuario.buscar_usuario_por_id(id)
        if usuario:
            return jsonify(usuario)
        else:
            return {"status": "ERRO", "mensagem": f"Erro ao obter usuario {id}"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter usuario"}

app.run()