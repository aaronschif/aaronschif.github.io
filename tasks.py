from invoke import run, task


@task
def build():
    pass


@task
def clean():
    run('rm -rf _build')


@task
def run():
    from builder import app
    app.run(debug=True)
