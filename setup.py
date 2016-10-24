from setuptools import setup, find_packages

VERSION = '0.0.2'


setup(
    name="sphinx-boost",
    version=VERSION,
    url='https://github.com/pfultz2/sphinx-boost',
    license='boost',
    description='Boost theme for sphinx',
    author='Paul Fultz II',
    author_email='pfultz2@yahoo.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
