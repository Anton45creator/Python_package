from setuptools import setup, find_packages

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='task5_python_package',
    version='0.1.0',
    url='https://git.foxminded.com.ua/Anton1/task5_python-package.git',
    license='proprietary',
    author='ThinkPad',
    author_email='Loukik56@mail.py',
    description='A program that counts unique characters in a string.',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

)
