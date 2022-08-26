"""
Set up
"""
from setuptools import setup, find_packages

#tests_require = ['nose2', 'coverage', 'lxml']

"""
This MUST match the repo name
If the repo name has dashes name
here should use underscores
"""
NAME = 'paloaltoapi'
__version__ = None
exec(open(f"{NAME}/_version.py").read())

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name=NAME, version=__version__,
      author="Adam",
      author_email="adam@tavnets.com",
      maintainer_email="adam@tavnets.com",
      packages=find_packages(),
      include_package_data=True,
      install_requires=requirements,
      # tests_require=tests_require,
      test_suite="tests",
      #extras_require={'testing': tests_require},
      url='https://github.com/atav928/paloaltoapi',
      keywords=['paloalto','firewall','panorama']
      )  # pragma: no cover
