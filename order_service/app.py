from flask import Flask
from .routes import order_bp
from .database import init_db

app = Flask(__name__)
app.register_blueprint(order_bp)

if __name__ == '__main__':
    init_db()
    app.run(port=5003, debug=True)
