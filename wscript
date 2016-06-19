from waflib import TaskGen, Task

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
    bld(source='src/sheep.svg', target='sheep.min.svg')
    bld(source='src/sheep.svg', target='sheep.png')
    bld(source='src/sheep.svg', target='sheep.ico', size='60x60')
    bld(rule='cp ${SRC} ${TGT}', source='src/aaron_schif.src.vcs', target='aaron_schif.vcs')

def _build_jade(tsk):
    from os.path import dirname, basename
    from jinja2 import Environment, Template, FileSystemLoader
    import pyjade
    assert len(tsk.inputs) == 1 and len(tsk.outputs) == 1
    src = tsk.inputs[0].abspath()
    tgt = tsk.outputs[0].get_bld()
    env = Environment(extensions=['pyjade.ext.jinja.PyJadeExtension'], loader=FileSystemLoader(dirname(src)))

    template = env.get_template(basename(src))
    tgt.write(template.render())


@TaskGen.extension('.svg')
def _build_image_magick(self, node):
    size = getattr(self, 'size', None)
    output = self.path.make_node(self.target)
    task = self.create_task('_ImageMagick')
    task.target = output.get_bld().abspath()
    task.source = node.abspath()
    task.opt_size = size


class _ImageMagick(Task.Task):
    def __str__(self):
        return self.__cmd()

    def __cmd(self):
        if self.opt_size is not None:
            cmd = 'convert -background none {src} -resize {size} {tgt}'
        else:
            cmd = 'convert -background none {src} {tgt}'
        return cmd.format(src=self.source, tgt=self.target, size=self.opt_size)

    def run(self):
        cmd = self.__cmd()
        self.exec_command(cmd)
