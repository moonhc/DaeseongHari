#!/usr/bin/env python
from flask.ext.script import Manager
from app import app

manager = Manager(app)

@manager.command
def run():
    """
    Run server
    """
    app.run("0.0.0.0", 5000)

if __name__ == '__main__':
    manager.run()
