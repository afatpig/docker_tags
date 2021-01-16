import os

from setuptools import find_packages, setup

# get the installation requirements:
with open('requirements.txt') as req:
    REQUIREMENTS = [line for line in req.read().split(os.linesep) if line]
    print(f"Requirements: {REQUIREMENTS}")

options = {
    'name': 'docker_tags',
    'version': '1.0.0',
    'description': 'List tags of a docker repo.',
    'url': '',
    'packages': find_packages(),
    'include_package_data': True,
    'zip_safe': False,
    'install_requires': REQUIREMENTS,
    'entry_points': {
        'console_scripts': [
            'dtags = docker_tags:main'
        ]
    },
}

setup(**options)
