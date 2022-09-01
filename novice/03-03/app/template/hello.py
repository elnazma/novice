from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index page"

@app.route("/hello")
def hello():
    return "Hello, world"

# @app.route('/user/user_name')
# def show_user_profile(user_name):
#     return f"User, (user_name)"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f"User, {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post, {post_id}"


if __name__ == "__main__":
    app.run()