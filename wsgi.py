# navbar for navigating in your app
# a hero section, out your avatar and your name and your title
# an about section describes who you are
# a portfolio section listing your projects (title,image,link)
# a footer , put your “Created by me with Flask” and your email

from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@application.route('/<user_name>')
def reader_user_name(user_name):
    return f"{user_name} is user_name"


# @application.route('/<user_name>/<app>')
# def renderer()

@application.route('/')
def index():
    return 'Index Page'

@application.route('/about')
def about():
    return 'About Page'
if __name__ == '__main__':
    application.run(debug=True)
