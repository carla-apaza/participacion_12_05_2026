from flask import render_template


def list(citas):
    return render_template("citas/index.html", citas=citas)


def create(medicos, pacientes):
    return render_template("citas/create.html", medicos=medicos, pacientes=pacientes)


def edit(cita, medicos, pacientes):
    return render_template(
        "citas/edit.html", cita=cita, medicos=medicos, pacientes=pacientes
    )
