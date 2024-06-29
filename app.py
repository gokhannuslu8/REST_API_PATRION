import json

from flask import Flask
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
from routes.factory_routes import factory_bp
from routes.entity_routes import entity_bp
from config import ConfigMongo

app = Flask(__name__)
app.config.from_object(ConfigMongo)

jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(factory_bp)
app.register_blueprint(entity_bp)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)


app.config.from_object(ConfigMongo)
app.json_encoder = CustomJSONEncoder


if __name__ == "__main__":
    app.run(debug=True)
