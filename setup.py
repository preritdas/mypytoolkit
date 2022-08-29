from setuptools import setup, find_packages

VERSION = "1.5.3"
DESCRIPTION = (
    "Basic tools I feel are missing in the standard Python distribution."
)


def get_read_me():
    with open("README.md", "r") as f:
        return f.read()


def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


# Setting up
setup(
    name="mypytoolkit",
    version=VERSION,
    author="Prerit Das",
    author_email="<preritdas@gmail.com>",
    description=DESCRIPTION,
    long_description=get_read_me(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires = read_requirements(),
    keywords=["python", "tools"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
