import  setuptools

with open("README.md", "r") as md:
    long_description = md.read()

setuptools.setup(
    name="rsgis",
    version="0.0.2",
    author="Emmanuel Jolaiya, Oke Mattew",
    author_email="jolaiyaemmanuel@gmail.com, matthewoke16@gmail.com",
    description="A python package for basic to advanced GIS operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeafreezy/rsgis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)