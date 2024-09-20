from setuptools import setup, find_packages

# Read the README file for long description
with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="file-structure-python-project",  # Replace with your project name
    version="1.0.0",  # Versioning: MAJOR.MINOR.PATCH
    author="",
    author_email="",
    description="A file-structure Python project for demonstration purposes.",
    long_description_content_type="text/x-rst",  # Content type of README
    url="https://github.com/yourusername/file-structure-python-project",
    packages=find_packages('src'),
    package_dir={'':'arc'} , 
    python_requires='>=3.6'
)
