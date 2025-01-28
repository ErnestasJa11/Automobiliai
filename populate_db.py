from app import app
from models import db, Automobilis

with app.app_context():
    # Išvalome duomenų bazę
    db.drop_all()
    db.create_all()

    # Sukuriame automobilius
    auto1 = Automobilis('BMW', 'X5', 'Juoda', 2020, 45000)
    auto2 = Automobilis('Audi', 'A6', 'Sidabrinė', 2019, 35000)
    auto3 = Automobilis('Toyota', 'Corolla', 'Balta', 2021, 25000)
    auto4 = Automobilis('Tesla', 'Model 3', 'Raudona', 2022, 55000)
    auto5 = Automobilis('Volkswagen', 'Golf', 'Mėlyna', 2018, 18000)

    # Įrašome į duomenų bazę
    db.session.add_all([auto1, auto2, auto3, auto4, auto5])
    db.session.commit()