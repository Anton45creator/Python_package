from setuptools import setup, find_packages

setup(
    name='python package',
    version='1.0',
    url='https://github.com/Anton45creator/Pathon_Package.git',
    license='Apache 2.0',
    author='ThinkPad',
    author_email='Loukik56@mail.ru',
    description='A program that counts unique characters in a string.',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
