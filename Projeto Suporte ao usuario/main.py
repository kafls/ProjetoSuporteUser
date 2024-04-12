from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

chamados = [
    {'id': 1, 'usuario': 'Karen', 'setor':'RH','desc': 'impressora deu pau','status':True},
]

# Rota para listar todos os chamados
@app.route('/getall', methods=['GET'])
def lista_chamados():
    return jsonify(chamados)

# Rota para obter um chamado pelo código
@app.route('/<int:id>', methods=['GET'])
def get_chamados(id):
  for chamado in chamados:
    if chamado['id'] == id:
      return jsonify(chamado)
    
  return jsonify({"error": "Chamado não encontrado"}), 404

# Rota para cadastrar chamado
@app.route('/novo', methods=['POST'])
def add_chamado():
  id = len(chamados) + 1
  cpf = request.form['cpf']
  usuario = request.form['usuario']
  setor = request.form['setor']
  desc = request.form['desc']
  novo_chamado = {"id": id, "cpf": cpf, "usuario": usuario, "setor": setor, "desc": desc, "status": True}
  chamados.append(novo_chamado)
  return jsonify({"message": "Usuário cadastrado"}), 201

# Rota para alterar informações do chamado
@app.route('/editar/<int:id>', methods=['PUT'])
def alterar(id):
  usuario = request.form['usuario']
  setor = int(request.form['setor'])
  desc = request.form['desc']
  for chamado in chamados:
    if chamado['id'] == id:
      chamado['usuario']=usuario
      chamado['setor']=setor
      chamado['desc']=desc
    return jsonify({"message": "Alterações realizadas"}), 201

# Rota para alterar status do usuário
@app.route('/status/<int:id>', methods=['GET'])
def edt_status(id):
  for chamado in chamados:
    if chamado['id'] == id:
      if chamado['ativo'] == True:
        chamado['ativo'] = False
      else:
        chamado['ativo'] = True
  return jsonify({"message": "Status alterado"}), 201 

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

