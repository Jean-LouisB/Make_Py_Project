from .write import write
from .init import Project


def run():
    project = Project()
    write(project)
