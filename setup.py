from setuptools import find_packages, setup

setup(
    name='hematopy',
    packages=find_packages(),
    version='0.0.1',
    entry_points = {
        'console_scripts': ['hematopy=src.haemapy.cli:haemapy_cli'],
    },
    description='Python and Blood',
    author='@ArgoCrew/ArgoPy',
    license='BSD-3',
)
