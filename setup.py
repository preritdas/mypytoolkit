from setuptools import setup, find_packages

VERSION = "0.0.2"
DESCRIPTION = (
    "A few basic tools I feel are missing in the standard Python distribution."
)

def getReadMe():
    with open("README.md", "r") as f:
        return f.read()

# Setting up
setup(
    name="mypytoolkit",
    version=VERSION,
    author="Prerit Das",
    author_email="<preritdas@gmail.com>",
    description=DESCRIPTION,
    long_description=getReadMe(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires = ["DateTime==4.4"],
    keywords=["python", "tools"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)