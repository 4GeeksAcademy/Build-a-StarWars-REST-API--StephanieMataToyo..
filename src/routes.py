from flask import Flask, request, jsonify, url_for, Blueprint
from models import Characters
from utils import APIException

api = Blueprint('api', __name__)

@api.route('/test' , methods=['GET'])
def testAPI():
    return jsonify('YOUR API WORKS'), 200

@api.route('/test' , methods=['POST'])
def postTest():
    return jsonify('THIS IS A POST RESPONSE'), 200

@api.route('/Characters' , methods=['POST'])
def add_Characters():
    return jsonify()

