from setuptools import setup, find_packages

def getFile(fileName):
    with open(fileName, "r") as fileHandler:
        return fileHandler.read()

setup(
    name="gg8-trafficlights",
    nersion="0.1.1",
    author="GloriousGlider8",
    author_email="sam.g.plimmer@gmail.com",
    description="A package to help prevent race conditions.",
    packages=find_packages(),
    long_description=getFile("README.md")
)