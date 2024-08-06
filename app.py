from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from pymongo import MongoClient
from environs import Env

# Load environment variables
env = Env()
env.read_env()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Flask-RESTful API
api = Api(app)

# Configure MongoDB connection
DATABASE_URL = env.str('DATABASE_URL')
PORT = env.int('PORT', default=4000)

client = MongoClient(DATABASE_URL)
db = client['mydatabase']
collection = db['mycollection']

# Define the Resource class for the API
class DataResource(Resource):
    def get(self):
        data = list(collection.find({}, {'_id': 0}))
        return jsonify(data)

# Add the resource to the API
api.add_resource(DataResource, '/api/data')

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
