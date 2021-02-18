from controllers.profiles_controller import profiles
from controllers.users_controller import auth
from controllers.post_controller import posts


registerable_controllers = [
    auth,
    profiles,
    posts
]