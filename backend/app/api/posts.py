# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse

from app.models import Post

class Posts(Resource):
    def get(self):
        posts = Post.query.order_by(Post.id.desc()).all()
        
        return {
            'success': True,
            'data': [
                post.to_dict() for post in posts
            ]
        }


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='This field is required')
        parser.add_argument('content', type=str, required=True, help='This field is required')
        args = parser.parse_args()
        
        post = Post(
            title   = args['title'],
            content = args['content']
        )
        
        post.save()
        
        return {
            'success': True,
            'data': post.to_dict()
        }, 201