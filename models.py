from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Automobilis(db.Model):
    __tablename__ = 'automobiliai'
    id = db.Column(db.Integer, primary_key=True)
    gamintojas = db.Column(db.String(50), nullable=False)
    modelis = db.Column(db.String(50), nullable=False)
    spalva = db.Column(db.String(50), nullable=False)
    metai = db.Column(db.Integer, nullable=False)
    kaina = db.Column(db.Float, nullable=False)

    def __init__(self, gamintojas, modelis, spalva, metai, kaina):
        self.gamintojas = gamintojas
        self.modelis = modelis
        self.spalva = spalva
        self.metai = metai
        self.kaina = kaina

    def __repr__(self):
        return f'{self.gamintojas} {self.modelis}'
