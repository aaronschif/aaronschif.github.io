top = '.'
out = 'build'


def configure(cfg):
    cfg.find_program('sassc', var='SASSC')
    cfg.find_program('pyjade', var='PYJADE')

def build(bld):
    bld(rule='${SASSC} ${SRC} ${TGT}', source='src/main.sass', target='main.noprefix.css')
    bld(rule='../node_modules/.bin/autoprefixer-cli ${SRC} -o ${TGT}', source='main.noprefix.css', target='main.css')
    bld(rule=_build_jade, source='src/index.jade', target='index.html')
    # bld(rule='wkhtmltopdf --print-media-type ${SRC} ${TGT}', source='index.html', target='resume.pdf')
    bld(rule='cp ${SRC} ${TGT}', source='src/sheep.svg', target='sheep.min.svg')
    bld(rule='cp ${SRC} ${TGT}', source='src/aaron_schif.src.vcs', target='aaron_schif.vcs')

def _build_jade(tsk):
    # import jinja2
    from os.path import dirname, basename
    from jinja2 import Environment, Template, FileSystemLoader
    import pyjade
    assert len(tsk.inputs) == 1 and len(tsk.outputs) == 1
    src = tsk.inputs[0].abspath()
    tgt = tsk.outputs[0].get_bld()
    env = Environment(extensions=['pyjade.ext.jinja.PyJadeExtension'], loader=FileSystemLoader(dirname(src)))

    template = env.get_template(basename(src))
    tgt.write(template.render())
