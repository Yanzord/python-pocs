from flask import Flask
from flask import jsonify
from flask import request
import repository

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_all_users():
  output = []
  for user in repository.get_all():
    output.append({'name' : user['name'], 'email' : user['email']})
  return jsonify({'result' : output})

@app.route('/user/<name>', methods=['GET'])
def get_one_user(name):
  user = repository.get_one(name)
  if user:
    output = {'name' : user['name'], 'email' : user['email']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/user', methods=['POST'])
def add_user():
  name = request.json['name']
  email = request.json['email']
  new_user = repository.add_one(name, email)
  output = {'name' : new_user['name'], 'email' : new_user['email']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)