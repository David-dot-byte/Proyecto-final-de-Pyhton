from flask import Flask, render_template, request, redirect, session
from models import db, User, Habit

app = Flask(__name__)

app.config["SECRET_KEY"] = "123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eco.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
        email=request.form["email"],
        password=request.form["password"]
        ).first()
        if user:
            session["user_id"] = user.id
            return redirect("/dashboard")
    return render_template("login.html")

# REGISTRO
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        u = User(
        username=request.form["username"],
        password=request.form["password"],
        email = request.form["email"]
        )

        db.session.add(u)
        db.session.commit()

        return redirect("/")

    return render_template("registro.html")

if __name__ == "__main__":
    app.run(debug=True)
