# coding: utf-8

from fabric.api import local, task

@task
def start():
    """
    Generates the slides from the markdown file and open the html in a browser
    """
    local("landslide presentation.cfg")
    local("xdg-open presentation.html")