from flask import Flask
from app.routes import form_bp
from app.database import init_db, db

app = Flask(__name__)
app.register_blueprint(form_bp, url_prefix='/form')

init_db(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)