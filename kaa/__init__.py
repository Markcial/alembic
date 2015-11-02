
from flask import Flask
from .routing.front import router as front_router

app = Flask(__name__)
app.register_blueprint(front_router)
