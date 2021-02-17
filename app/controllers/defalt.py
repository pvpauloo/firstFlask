from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm, Register


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
            flash("Logged in.")
        else:
            flash("Invalid login")

    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))



@app.route("/register", methods=["POST", "GET"])
def register():
    form = Register()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            flash("Username or e-mail conflits.")
        else:
            insert = User(form.username.data, form.password.data, form.name.data, form.email.data)
            db.session.add(insert)
            db.session.commit()
            return redirect(url_for("login"))
            flash("Register Sucess")

    return render_template('register.html', form=form)



@app.route("/crud/<info>")
@app.route("/crud", defaults={"info": None})
def crud(info):
    # CREATE
    insert = User("suko_maia", "1234", "Emerson Maia", "emrodrigues17@gmail.com")
    db.session.add(insert)
    db.session.commit()

    # # READ
    # read = User.query.filter_by(username="suko_maia").first()
    # print(read.username, read.name, read.email)

    # # UPDATE
    # update = User.query.filter_by(username="pvpauloo").first()
    # update.password = "update_Senha"
    # db.session.add(update)
    # db.session.commit()
    #
    # # DELETE
    # delete = User.query.filter_by(username="suko_maia").first()
    # db.session.delete(delete)
    # db.session.commit()

    return "ok"