from main import db
from flask import Blueprint



db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Profiles import Profiles
    from faker import Faker
    from models.Users import Users
    from main import bcrypt
    from models.Post import Post
    from models.Messages import Messages
    import random

    faker = Faker()
    profiles = []
    true_or_false = [True, False]
    posts = []

    for i in range(10):
        user = Users()
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        #accounts.append(user)
    db.session.commit()



    for i in range(10):
        profile = Profiles()
        profile.username = faker.name()
        profile.fname = faker.first_name()
        profile.lname = faker.last_name()
        profile.account_active=faker.boolean()
        profile.user_id = i+1
        profile.github=faker.name()
        profile.front_end = random.choice(true_or_false)
        profile.back_end = random.choice(true_or_false)
        profile.full_stack = random.choice(true_or_false)
        db.session.add(profile)
        profiles.append(profile)
    db.session.commit()

    for i in range(30):
        new_post = Post()
        new_post.post_name = faker.name()
        new_post.post_description = faker.catch_phrase()
        new_post.account_active = random.choice(true_or_false)
        new_post.front_end = random.choice(true_or_false)
        new_post.back_end = random.choice(true_or_false)
        new_post.full_stack = random.choice(true_or_false)
        new_post.completed = random.choice(true_or_false)
        new_post.post_github = faker.url()
        new_post.profile_id = random.choice(profiles).profileid
        posts.append(new_post)
        db.session.add(new_post)
    db.session.commit()
        
    for i in range(50):
        new_message = Messages()
        new_message.post_id = random.choice(posts).postid
        new_message.profile_id = random.choice(profiles).profileid
        new_message.messages = faker.catch_phrase()
        new_message.timestamp = faker.date_between(start_date = "-1y", end_date = "+1y")
        db.session.add(new_message)
    db.session.commit()

    print("Tables seeded")