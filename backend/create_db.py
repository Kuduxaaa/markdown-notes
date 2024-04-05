#!/bin/python3
# -*- coding: utf-8 -*-

from app import app, db
from app.models import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
