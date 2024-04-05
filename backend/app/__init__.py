# -*- coding: utf-8 -*-

import config

from flask import Flask, jsonify

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(config.ProductionConfig)

cors = CORS(app)
api_router = Api(app, prefix='/api/v1')
db = SQLAlchemy(app)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'error': 'Page not found',
        'code': 404,
        'success': False
    }), 404


from app.api.posts import Posts
from app.api.single_post import SinglePost

api_router.add_resource(Posts, '/posts')
api_router.add_resource(SinglePost, '/posts/<id>')
