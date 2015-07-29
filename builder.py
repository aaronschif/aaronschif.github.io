from jinja2 import Environment, FileSystemLoader
from markdown import markdown
import sass
from flask import Flask

env = Environment(
    loader=FileSystemLoader('templates'),
    extensions=['pyjade.ext.jinja.PyJadeExtension'],
    cache_size=0
    )


app = Flask(__name__)

@app.route("/")
def home():
    template = env.get_template('home.jade')
    return template.render()

@app.route("/resume")
def resume():
    template = env.get_template('resume.jade')
    return template.render()

@app.route("/main.css")
def css():
    return sass.compile_file('static/main.sass'), 200, {'Content-Type': 'text/css; charset=utf-8'}

if __name__ == "__main__":
    app.run(debug=True)
