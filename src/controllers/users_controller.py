from schemas.UsersSchema import user_schema, users_schema
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for
from models.Users import Users
from main import bcrypt, db
#from flask_jwt_extended import create_access_token
from flask_login import login_user, current_user, logout_user, login_required  #added
from datetime import timedelta

auth = Blueprint('auth', __name__)

@auth.route("/home", methods=["GET"])   
@auth.route("/", methods=["GET"])                   #added
def main_page():
    # return redirect(url_for('post.post_index'))
    return render_template('home.html')

@auth.route('/signup', methods=['GET']) #added'
def signup():
    return render_template('signup.html')

@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('post.post_index'))

@auth.route("/register", methods=["POST"])
def auth_register():
    email = request.form.get('email')
    password = request.form.get('password')
  
    #user_fields = user_schema.load(request.json)

    user = Users.query.filter_by(email=email).first()

    if user:
        return abort(400, description="User already")


# @auth.route('/signup', methods=[GET])
# def signup():
#     return render_template('signup.html')
    
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
    #user.email = user_fields["email"]
   # user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    user.email = email
    user.password = bcrypt.generate_password_hash(password).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    #return jsonify(user_schema.dump(user))
    return redirect(url_for('auth.login'))  #added


@auth.route("/login", methods=["POST"])
def auth_login():

    email = request.form.get('email')
    password = request.form.get('password')
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

    #user_fields = user_schema.load(request.json)

    user = Users.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):  #changed
        return abort(401, description="Incorrect username and password")
    login_user(user)
    print(current_user.email)

    #expiry = timedelta(days=1)
    #access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

    #return jsonify({ "token": access_token })
    return redirect(url_for('post.post_index'))

   