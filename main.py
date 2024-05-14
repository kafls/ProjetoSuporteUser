from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

chamados = [
    {'id': 1, 'usuario': 'Karen', 'setor':'RH','desc': 'impressora deu pau','status':True, 'cpf': 47518605856, 'comentario':'testando'},
]

id = 1

# Rota para listar todos os chamados
@app.route('/getall', methods=['GET'])
def lista_chamados():
    return jsonify(chamados)

# Rota para obter um chamado pelo código
@app.route('/<int:cpf>', methods=['GET'])
def get_chamado(cpf):
  for chamado in chamados:
    if chamado['cpf'] == cpf:
      return jsonify(chamado)
  return jsonify({"error": "Chamado não encontrado"}), 404

# Rota para cadastrar chamado 
@app.route('/novo', methods=['POST'])
def add_chamado():
  global id
  id += 1
  cpf = request.form['cpf']
  usuario = request.form['usuario']
  setor = request.form['setor']
  desc = request.form['desc']
  novo_chamado = {"id": id, "cpf": cpf, "usuario": usuario, "setor": setor, "desc": desc, "status": True}
  chamados.append(novo_chamado)

  novo_chamado = {
        "id": id,
        "usuario": usuario,
        "cpf": cpf,
        "setor": setor,
        "desc": desc,
        "status": True,
        "comentario": ""
    }

  return jsonify({"message": "Usuário cadastrado"}), 201

# Rota para alterar informações do chamado
@app.route('/editar/<int:id>', methods=['POST'])
def alterar(id):
  usuario = request.form['usuario']
  cpf = request.form['cpf']
  setor = int(request.form['setor'])
  desc = request.form['desc']
  comentario = request.form['comentario']

  for chamado in chamados:
    if chamado['id'] == id:
      chamado['usuario']=usuario
      chamado['setor']=setor
      chamado['desc']=desc
      chamado['cpf']=cpf
      chamado['comentario']=comentario
    return jsonify({"message": "Alterações realizadas"}), 201


# Rota para alterar status do usuário
@app.route('/status/<int:id>', methods=['POST'])
def edt_status(id):
  for chamado in chamados:
    dados = request.json
    comentario = dados.get('comentario')
    if chamado['id'] == id:
      chamado['comentario']=comentario
      if chamado['status'] == True:
        chamado['status'] = False
      else:
        chamado['status'] = True
        
      return jsonify({"message": "Status alterado"}), 201
  return jsonify({"message": "ID não encontrado"}), 404

# Rota para excluir um chamado
@app.route('/deletar/<int:id>', methods=['DELETE'])
def deletar_chamado(id):
  for chamado in chamados:
    if chamado['id'] == id:
      chamados.remove(chamado)
      return jsonify({'message': 'Chamado deletado com sucesso'}), 200
  else:
    return jsonify({'error': 'Chamado não encontrado'}), 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)

