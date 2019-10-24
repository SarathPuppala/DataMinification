import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DataMinification",
    version="0.0.1",
    author="Sarath Puppala",
    author_email="sarathpuppala1993@gmail.com",
    description="This Package is mainly used to reduce the memory size of Datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SarathPuppala/DataMinification",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)