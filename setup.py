import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='thumbor_extras',
    version='0.1',
    author="Austin Blanton",
    author_email="imaus10@gmail.com",
    description="Some useful extensions to thumbor - extra filters and detectors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imaus10/thumbor_extras",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2 :: Only", # pending thumbor's upgrade to python3
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
 )
