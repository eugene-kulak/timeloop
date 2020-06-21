# please install python if it is not present in the system
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='timeloop',
    version='1.0.4',
    packages=['timeloop'],
    license='MIT',
    description='An elegant way to run period tasks.',
    author='Eugene Kulak',
    author_email='kulak.eugene@gmail.com',
    keywords=['tasks', 'jobs', 'periodic task', 'interval', 'periodic job', 'decorator'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eugene-kulak/timeloop",
    include_package_data=True,
)
