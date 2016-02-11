from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from webassets import Environment as AssetsEnvironment
from os.path import abspath, dirname

import cherrypy

BASE_PATH = Path(__file__).parent

env = Environment(
    loader=FileSystemLoader('templates'),
    extensions=[
        'pyjade.ext.jinja.PyJadeExtension',
        'webassets.ext.jinja2.AssetsExtension'
    ],
    cache_size=0
)

assets_env = AssetsEnvironment(
    debug=True,
    url='/static',
    directory=str(BASE_PATH/'var/static/'),
    load_path=[str(BASE_PATH/'static/')]
)
env.assets_environment = assets_env

assets_env.register(
    'css',
    'main.sass',
    output='main.css',
    filters='libsass',
)


if __name__ == '__main__':
    BASE_PATH.joinpath('var/index.html').write_text(env.get_template('home.jade').render())
    BASE_PATH.joinpath('var/resume.html').write_text(env.get_template('resume.jade').render())




# class Router(object):
#     @cherrypy.expose
#     def index(self):
#         template = env.get_template('home.jade')
#         template = env.get_template('resume.jade')
#         return template.render()
#
#     @cherrypy.expose
#     def resume(self):
#         template = env.get_template('resume.jade')
#         return template.render()
#
# if __name__ == '__main__':
#     conf = {
#         '/static': {
#             'tools.staticdir.on': True,
#             'tools.staticdir.dir': BASE_PATH+'/var/static/'
#         }
#     }
#     cherrypy.quickstart(Router(), '/', conf)
