from flask import Flask, request, render_template
from controllers import (
    medico_controller,
    consulta_controller,
    cita_controller,
    paciente_controller,
)
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinica.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(medico_controller.medico_bp)
app.register_blueprint(consulta_controller.consulta_bp)
app.register_blueprint(cita_controller.cita_bp)
app.register_blueprint(paciente_controller.paciente_bp)


@app.context_processor
def inject_active_path():
    def is_active(path):
        return "active" if request.path == path else ""

    return dict(is_active=is_active)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
