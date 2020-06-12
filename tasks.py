from invoke import task
import os


@task
def serve(c):
    re_exec("pelican content -l -r -t theme -b 0.0.0.0")


@task
def build(c):
    c.run("pelican content -t theme")
    c.run("rm -rf output/theme/.webassets-cache")


def re_exec(cmd):
    args = cmd.split(" ")
    os.execvp(args[0], args)
