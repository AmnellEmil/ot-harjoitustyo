from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/minesweeper.py")

@task
def test(ctx):
    print("working")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
