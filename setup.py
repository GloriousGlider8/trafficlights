from setuptools import setup, find_packages

def getFile(fileName):
    with open(fileName, "r") as fileHandler:
        return fileHandler.read()

setup(
    name="trafficlights",
    version="0.1.1",
    author="GloriousGlider8",
    author_email="sam.g.plimmer@gmail.com",
    description="A package to help prevent race conditions.",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    long_description=getFile("README.md")
)