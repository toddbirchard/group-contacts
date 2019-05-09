"""Contact grouper setup."""

from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Contact Grouper',  # Required
    version='0.0.1',  # Required
    description='Group list of contacts by phone number.',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/toddbirchard/group-contacts',  # Optional
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Contacts Group',  # Optional
    packages=find_packages(),
    install_requires=['toolz'],
    entry_points={
        'console_scripts': [
            'main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/toddbirchard/group-contacts/issues',
        'Source': 'https://github.com/toddbirchard/group-contacts/',
    },
)
