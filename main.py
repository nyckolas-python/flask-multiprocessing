#!/usr/bin/python3
from app import app as application
from app import db


import views

if __name__ == '__main__':
    application.run()