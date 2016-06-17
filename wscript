top = '.'
out = 'build'


def configure(cfg):
    cfg.find_program('sassc', var='SASSC')
    cfg.find_program('pyjade', var='PYJADE')

def build(bld):
    bld(rule='${SASSC} ${SRC} ${TGT}', source='src/main.sass', target='src/main.noprefix.css')
    bld(rule='../node_modules/.bin/autoprefixer-cli ${SRC} -o ${TGT}', source='src/main.noprefix.css', target='src/main.css')
    bld(rule=_build_jade, source='src/index.jade', target='src/index.html')
    bld(rule='wkhtmltopdf --print-media-type ${SRC} ${TGT}', source='src/index.html', target='src/resume.pdf')

def _build_jade(tsk):
    # import jinja2
    from os.path import dirname, basename
    from jinja2 import Environment, Template, FileSystemLoader
    import pyjade
    assert len(tsk.inputs) == 1 and len(tsk.outputs) == 1
    src = tsk.inputs[0].abspath()
    tgt = tsk.outputs[0]
    env = Environment(extensions=['pyjade.ext.jinja.PyJadeExtension'], loader=FileSystemLoader(dirname(src)))

    template = env.get_template(basename(src))
    # template = Template(src.read())
    tgt.write(template.render())
