"""
This script runs the FlaskTest application using a development server.
"""

from os import environ
from FlaskTest import application

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run()


#if __name__ == '__main__':
#    HOST = environ.get('SERVER_HOST', 'localhost')
#    try:
#        PORT = int(environ.get('SERVER_PORT', '5555'))
#    except ValueError:
#        PORT = 5555
#    application.run(HOST, PORT)
