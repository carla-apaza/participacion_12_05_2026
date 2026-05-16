from database import db


class Cita(db.Model):
    __tablename__ = "citas"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20), nullable=False)
    hora = db.Column(db.String(10), nullable=False)
    motivo = db.Column(db.String(10), nullable=False)

    id_medico = db.Column(db.Integer, db.ForeignKey("medicos.id"), nullable=False)

    id_paciente = db.Column(db.Integer, db.ForeignKey("pacientes.id"), nullable=False)

    medico = db.relationship("Medico")
    paciente = db.relationship("Paciente")

    def __init__(self, fecha, hora, motivo, id_medico, id_paciente):

        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.id_medico = id_medico
        self.id_paciente = id_paciente

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cita.query.all()

    @staticmethod
    def get_by_id(id):
        return Cita.query.get(id)

    def update(
        self, fecha=None, hora=None, motivo=None, id_medico=None, id_paciente=None
    ):

        if fecha:
            self.fecha = fecha

        if hora:
            self.hora = hora

        if motivo:
            self.motivo = motivo

        if id_medico:
            self.id_medico = id_medico

        if id_paciente:
            self.id_paciente = id_paciente

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
