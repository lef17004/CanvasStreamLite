from bottle import route, run, static_file, request, post
from application.main import Main
from application.event import ClientToServer

applications = {}

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
    main = Main()
    response = main.setup(setup_info)
    session_key = main.session_key
    applications[session_key] = main

    return {'instructions' :response.instructions}

@post("/event/<session_key>")
def event(session_key):
    message = ClientToServer(request.json)
    response = applications[str(session_key)].loop(message)
    return {'instructions': response.instructions}

@route("/disconnect/<session_key>")
def disconnect(session_key):
    return {}

run(host='localhost', port=8080, debug=True)











# @app.route("/image")
# def image():
#     return {
#         "url" : url_for('static', filename='images/invader.png')
#     }
