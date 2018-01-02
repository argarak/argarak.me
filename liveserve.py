
from livereload import Server, shell
from common import app

app.debug = True

server = Server(app.wsgi_app)
server.serve(port=5000)
