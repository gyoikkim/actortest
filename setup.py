# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'python'}

packages = \
['actortest', 'actortest.actor', 'actortest.actor.commands']

package_data = \
{'': ['*'], 'actortest': ['etc/*']}

install_requires = \
['sdss-access>=0.2.3', 'sdss-tree>=2.15.2', 'sdsstools>=0.4.0']

entry_points = \
{'console_scripts': ['actortest = actortest.__main__:main']}

setup_kwargs = {
    'name': 'sdss-actortest',
    'version': '0.1.0a0',
    'description': 'test package for communicating with clu',
    'long_description': '# actortest\n\n![Versions](https://img.shields.io/badge/python->3.7-blue)\n[![Documentation Status](https://readthedocs.org/projects/sdss-actortest/badge/?version=latest)](https://sdss-actortest.readthedocs.io/en/latest/?badge=latest)\n[![Travis (.org)](https://img.shields.io/travis/sdss/actortest)](https://travis-ci.org/sdss/actortest)\n[![codecov](https://codecov.io/gh/sdss/actortest/branch/main/graph/badge.svg)](https://codecov.io/gh/sdss/actortest)\n\ntest package for communicating with clu\n',
    'author': 'Gyoik Kim',
    'author_email': 'gyoik_kim@khu.ac.kr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sdss/actortest',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)

# This setup.py was autogenerated using poetry.
