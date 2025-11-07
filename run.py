from flask import Flask, render_template
from app.routes import form_bp
from app.database import init_db, db
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(form_bp, url_prefix='/form')

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

init_db(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)