from setuptools import setup, find_packages

setup(
    name='python package',
    version='1.0',
    url='https://github.com/Anton45creator/Pathon_Package.git',
    license='Apache 2.0',
    author='ThinkPad',
    author_email='Loukik56@mail.ru',
    description='The package contains a command-line program that opens text '
            'files and counts the number of unique characters in a string. '
            'It also counts the number of characters in the entered string.',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
