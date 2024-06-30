import json
from flask import Flask
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
from routes.factory_routes import factory_bp
from routes.entity_routes import entity_bp
from config import ConfigMongo

# Uygulama oluşturuluyor ve yapılandırılıyor
app = Flask(__name__)
app.config.from_object(ConfigMongo)

# JWT yöneticisi oluşturuluyor
jwt = JWTManager(app)

# Blueprint'ler kaydediliyor
app.register_blueprint(auth_bp)
app.register_blueprint(factory_bp)
app.register_blueprint(entity_bp)


# Özel JSON Encoder tanımlanıyor
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)


# JSON Encoder uygulamaya ekleniyor
app.json_encoder = CustomJSONEncoder

# Uygulama çalıştırılıyor
if __name__ == "__main__":
    app.run(debug=True)
