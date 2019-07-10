import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="function-profiler",
    version="0.1.0",
    description="Profile a function using a simple decorator",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/asanoryu/function_profile",
    author="Vladislav Shumanov",
    author_email="vl.shumanov@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["function_profile"],
    include_package_data=True,
    install_requires=["memory_profiler"],
)
