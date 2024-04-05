# -*- coding: utf-8 -*-

from app import db

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True


    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content.replace('\\n', '\n').replace("\\'", "'")
        }
    

    def __repr__(self):
        return '<Post %r>' % self.title
