from flask import Blueprint
from schemas.UsersSchema import user_schema, users_schema
from flask import Blueprint, request, jsonify, abort
from models.Users import Users
from main import bcrypt, db
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)

    user = Users.query.filter_by(email=user_fields["email"]).first()

    if user:
        return abort(400, description="User already")
    
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))

    # form = RegistrationForm()

    # if form.validate_on_submit():
    #     user = Users()
    #     user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     user.email = form.email.data
    #     #user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    #     db.session.add(user)
    #     db.session.commit()
    #     flash('Your account has been created! You are now able to log in', 'success')
    #     return redirect(url_for('login'))

    # return render_template('register.html', title='Register', form=form)

    user = Users()
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))


@auth.route("/login", methods=["POST"])
def auth_login():

    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=form.remember.data)
    #         next_page = request.args.get('next')
    #         expiry = timedelta(days=1)
    #         access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    #         return redirect(next_page) if next_page else redirect(url_for('home'))
    #     else:
    #         flash('Login Unsuccessful. Please check email and password', 'danger')
    # return render_template('login.html', title='Login', form=form)

    user_fields = user_schema.load(request.json)

    user = Users.query.filter_by(email=user_fields["email"]).first()

    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username and password")

    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

    return jsonify({ "token": access_token })