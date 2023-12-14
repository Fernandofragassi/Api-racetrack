from flask import Flask, jsonify, request
from bd import racetrack
app = Flask(__name__)

#Lista todas as chaves da API
@app.route('/racetrack',methods=['GET'])

def get_racetrack():
    return jsonify(racetrack)



#Lista apenas a chave que corresponde ao ID passado na URL /racetrack/x
#for para verificar qual ID o usuário passou
@app.route('/racetrack/<int:id>',methods=['GET'])
def get_racetrack_by_id(id):
    for race in racetrack:
        if race.get('id') == id:
            return jsonify(race)


#Modifica um chave do json, verificação feita pelo ID
#for interage com ID passado pelo usuário e altera o index que o mesmo quis modificar
@app.route('/racetrack/<int:id>', methods=['PUT'])
def modify_racetrack_by_id(id):
    racetrack_modify = request.get_json()
    for index,race in enumerate(racetrack):
        if race.get('id') == id:
            racetrack[index].update(racetrack_modify)
            return jsonify(racetrack[index])


#Cria uma nova chave no json
@app.route('/racetrack', methods=['POST'])
def creat_racetrack():
    new_racetrack = request.get_json()
    racetrack.append(new_racetrack)
    return jsonify(racetrack)

#Deleta uma chave, a interação é feita pelo ID
@app.route('/racetrack/<int:id>',methods=['DELETE'])
def delete_racetrack(id):
    for index,race in enumerate(racetrack):
        if race.get('id') == id:
            del racetrack[index]
            return jsonify(racetrack)

#Modificar a porta caso está conflitando
app.run(port=5000,host='localhost',debug=True)