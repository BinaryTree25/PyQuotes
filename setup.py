from setuptools import setup, find_packages

setup(
    name="pyquotes",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="BinaryTree",
    author_email="binarytree25@gmail.com",
    description="A simple library to get programming-related quotes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BinaryTree25/pyquotes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)