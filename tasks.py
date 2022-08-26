from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def simulate_fast(ctx):
    ctx.run("python3 src/simulation.py 5 0.5")

@task
def simulate_normal(ctx):
    ctx.run("python3 src/simulation.py 7 5")

@task
def simulate_full(ctx):
    ctx.run("python3 src/simulation.py 7 30")

@task
def test(ctx):
    ctx.run("pytest")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")