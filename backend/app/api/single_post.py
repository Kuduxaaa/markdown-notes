# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse

from app.models import Post

class SinglePost(Resource):
    def get(self, id):
        post = Post.query.get(id)
        
        if post is None:
            return {'success': False, 'error': 'Post not found'}, 404
        
        return {
           'success': True,
            'data': post.to_dict()
        }


    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='This field is required')
        parser.add_argument('content', type=str, required=True, help='This field is required')
        args = parser.parse_args()
        
        post = Post.query.get(id)
        
        if post is None:
            return {'success': False, 'error': 'Post not found'}, 404
        
        post.title = args['title']
        post.content = args['content']
        
        post.save()
        
        return {'success': True}, 201
    
    
    def delete(self, id):
        post = Post.query.get(id)
        
        if post is None:
            return {'success': False, 'error': 'Post not found'}, 404
        
        post.delete()
        
        return {'success': True}, 204