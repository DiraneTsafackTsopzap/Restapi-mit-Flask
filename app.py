# from my_flask_app import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# # if __name__ == '__main__':
# #     app.run(debug=True)

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Définition de la ressource HelloWorld
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Bonjour Dirane Serges'}

# Définition de la ressource MeinUser
class MeinUser(Resource):
    def get(self):
        return {'numero de telephone': "98187298"}

# Association des ressources à des routes
api.add_resource(HelloWorld, '/')
api.add_resource(MeinUser, '/meinuser')

if __name__ == '__main__':
    app.run(debug=True)


# installaer dabord pip install flask-restful 