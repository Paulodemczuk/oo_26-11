from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.conta_controller import conta_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(conta_routes)
