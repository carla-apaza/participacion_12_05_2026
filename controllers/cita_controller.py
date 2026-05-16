from flask import request, url_for, redirect, Blueprint
from datetime import datetime

from models.cita_model import Cita
from models.medico_model import Medico
from models.paciente_model import Paciente

from views import cita_view

cita_bp = Blueprint("cita", __name__, url_prefix="/citas")


@cita_bp.route("/")
def index():
    citas = Cita.get_all()
    return cita_view.list(citas)


@cita_bp.route("/create", methods=["GET", "POST"])
def create():
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    if request.method == "POST":
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        motivo = request.form["motivo"]
        id_medico = request.form["id_medico"]
        id_paciente = request.form["id_paciente"]
        cita = Cita(fecha, hora, motivo, id_medico, id_paciente)
        cita.save()
        return redirect(url_for("cita.index"))
    return cita_view.create(medicos, pacientes)


@cita_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cita = Cita.get_by_id(id)
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    if request.method == "POST":
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        motivo = request.form["motivo"]
        id_medico = request.form["id_medico"]
        id_paciente = request.form["id_paciente"]
        cita.update(
            fecha=fecha,
            hora=hora,
            motivo=motivo,
            id_medico=id_medico,
            id_paciente=id_paciente,
        )
        return redirect(url_for("cita.index"))
    return cita_view.edit(cita, medicos, pacientes)


@cita_bp.route("/delete/<int:id>")
def delete(id):
    cita = Cita.get_by_id(id)

    cita.delete()

    return redirect(url_for("cita.index"))
