
# -*- encoding: utf-8 -*-
import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='hematopy',
    description='Python and Blood',
    version='0.0.2.dev1',
    author='Gustavo RPS @ ArgoCrew/ArgoPy',
    author_email='gustavorps+hematopy@argocrew.io',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    install_requires=[
        'CairoSVG==2.5.1',
        'click==6.7',
        'sanic==0.8.3',
        'lxml==4.2.1',
        'python-magic==0.4.15',
        'google-cloud-storage==1.10.0'
    ],
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
