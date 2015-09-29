from invoke import run, task


@task
def build():
    pass


@task
def clean():
    run('rm -rf var')


@task(name='run')
def run_():
    run('python builder.py')
