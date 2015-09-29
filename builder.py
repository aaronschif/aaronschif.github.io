from jinja2 import Environment, FileSystemLoader
from webassets import Environment as AssetsEnvironment
from os.path import abspath, dirname

import cherrypy

BASE_PATH = dirname(abspath(__file__))

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
    directory=BASE_PATH+'/var/static/',
    load_path=[BASE_PATH+'/static/']
)
env.assets_environment = assets_env


class Router(object):
    @cherrypy.expose
    def index(self):
        template = env.get_template('home.jade')
        return template.render()

    @cherrypy.expose
    def resume(self):
        template = env.get_template('resume.jade')
        return template.render()

if __name__ == '__main__':
    conf = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': BASE_PATH+'/var/static/'
        }
    }
    cherrypy.quickstart(Router(), '/', conf)
