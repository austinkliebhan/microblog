from app import app, db, cli
from app.models import User, Post

# The flask application instance is called app and is a member of the app package.


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
