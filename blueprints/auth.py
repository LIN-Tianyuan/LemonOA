from flask import Blueprint, render_template, jsonify, redirect, url_for, session
from exts import mail, db
# pip install flask-mail
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCaptchaModel, UserModel
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("Email does not exist in the database!")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                # cookie:
                # Cookies are not suitable for storing too much data, only a small amount of data
                # Cookies are generally used to store login authorization stuff
                # The session in flask, which is encrypted and stored in a cookie
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("Wrong password.")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))


# GET, Get data from the server
# POST, Submit client data to the server
@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # Verify that the email address and verification code submitted by the user correspond and are correct
        # Form Validation: flask-wtf: wtforms
        # pip install flask-wtf
        # pip install email_validator
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# bp.route: If no methods parameter is specified, the default is a GET request
@bp.route("/captcha/email")
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get("email")
    # 4/6：Arrays, letters, combinations of arrays and letters
    source = string.digits * 4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    message = Message(subject="Lemon OA Registration Verification Code", recipients=[email], body=f"Your verification code is : {captcha}")
    mail.send(message)
    # memcached/redis
    # Store as a database table
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTFUL API
    # {code: 200/400/500, message: "", data: {}}
    return jsonify({"code": 200, "message": "", "data": None})


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="test", recipients=["804233992@qq.com"], body="ceshi")
    mail.send(message)
    return "Email sent successfully!"
