
# -*- encoding: utf-8 -*-
import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().split('\n')

setuptools.setup(
    name='hematopy',
    description='Python and Blood',
    version='0.0.1.dev9',
    author='Gustavo RPS @ ArgoCrew/ArgoPy',
    author_email='gustavorps+hematopy@argocrew.io',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    # package_dir={'':'hematopy'},
    entry_points = {
        'console_scripts': [
            'hematopy=hematopy.cli:main'
        ],
    },
    license='BSD-3',
    keywords='blood banner utility',
    project_urls={
        'Issues': 'https://github.com/ArgoCrew/hematopy/issues',
        'Source Code': 'https://github.com/ArgoCrew/hematopy',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Intended Audience :: Healthcare Industry',
    ],
)
