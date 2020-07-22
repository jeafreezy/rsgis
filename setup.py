import  setuptools

with open("README.md", "r") as md:
    long_description = md.read()

setuptools.setup(
    name="rsgis",
    version="0.0.1",
    author="Emmanuel Jolaiya",
    author_email="jolaiyaemmanuel@gmail.com",
    description="A python package for basic GIS operations",
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