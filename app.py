from flask import Flask, render_template, request, redirect, url_for
from models import db, Automobilis

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_text = request.args.get("search")
    if search_text:
        filtered_cars = Automobilis.query.filter(
            (Automobilis.gamintojas.ilike(f"%{search_text}%")) |
            (Automobilis.modelis.ilike(f"%{search_text}%"))
        )
        return render_template("index.html", cars=filtered_cars)
    else:
        all_cars = Automobilis.query.all()
        return render_template("index.html", cars=all_cars)


@app.route("/automobilis/<int:id>")
def one_car(id):
    car = Automobilis.query.get(id)
    if car:
        return render_template("one_car.html", car=car)
    else:
        return f"Automobilio su ID {id} nėra"


@app.route("/automobilis/naujas", methods=["GET", "POST"])
def create_car():
    if request.method == "GET":
        return render_template("create_car.html")
    if request.method == "POST":
        gamintojas = request.form.get("gamintojas")
        modelis = request.form.get("modelis")
        spalva = request.form.get("spalva")
        metai = int(request.form.get("metai"))
        kaina = float(request.form.get("kaina"))

        if all([gamintojas, modelis, spalva, metai, kaina]):
            new_car = Automobilis(gamintojas, modelis, spalva, metai, kaina)
            db.session.add(new_car)
            db.session.commit()
        return redirect(url_for('home'))


@app.route("/automobilis/redaguoti/<int:id>", methods=["GET", "POST"])
def update_car(id):
    car = Automobilis.query.get(id)
    if not car:
        return f"Automobilio su ID {id} nėra"

    if request.method == "GET":
        return render_template("update_car.html", car=car)
    elif request.method == "POST":
        car.gamintojas = request.form.get("gamintojas")
        car.modelis = request.form.get("modelis")
        car.spalva = request.form.get("spalva")
        car.metai = int(request.form.get("metai"))
        car.kaina = float(request.form.get("kaina"))
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/automobilis/trinti/<int:id>", methods=["POST"])
def delete_car(id):
    car = Automobilis.query.get(id)
    if car:
        db.session.delete(car)
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
