from bottle import route, run, static_file, request, post
from application.application import Application
from application.server import Server
from application.event import ClientToServer

server = Server()

@route('/hello')
def hello():
    return "Hello World!"

@route('/')
def default():
    return static_file("index.html", root='static')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@post('/setup/')
def setup():
    setup_info = request.json
    app = server.start_application()
    
    response = app.setup(setup_info)

    return {'instructions' :response.instructions}

@post("/event/<session_key>")
def event(session_key):
    message = ClientToServer(request.json)
    app = server.get_session(session_key)
    response = app.loop(message)
    return {'instructions': response.instructions}

@route("/disconnect/<session_key>")
def disconnect(session_key):
    return {}

run(host='localhost', port=8081, debug=True)











# @app.route("/image")
# def image():
#     return {
#         "url" : url_for('static', filename='images/invader.png')
#     }
