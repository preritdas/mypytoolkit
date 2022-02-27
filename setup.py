from setuptools import setup, find_packages

VERSION = "1.0.1"
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
    install_requires = ["DateTime==4.4", "matplotlib==3.5.1", "numpy==1.22.0"],
    keywords=["python", "tools"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)