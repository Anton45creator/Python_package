from setuptools import setup, find_packages

setup(
    name='cli',
    version='1.0',
    url='https://git.foxminded.com.ua/Anton1/task5_python-package.git',
    author='Anton Viazovik',
    author_email='Loukik56@mail.ru',
    description='A program that counts unique characters in a string.',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
