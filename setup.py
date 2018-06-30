import os
from setuptools import setup, find_packages


def read_file(filename):
	basepath = os.path.dirname(os.path.dirname(__file__))
	filepath = os.path.join(basepath, filename)
	if os.path.exists(filepath):
		return open(filepath).read()
	else:
		return ''


setup(
	name='pepgraph',
	version='0.0.3',
	description='This is a tool for getting reference relation of PEP.',
	long_description=read_file('README.rst'),
	author='komo_fr',
	author_email='komofr.python@gmail.com',
	url='https://github.com/komo-fr/pepgraph',
	classifiers=[
	'Development Status :: 1 - Planning',
	'Programming Language :: Python',
    'Programming Language :: Python :: 3.6'
	],
	packages=find_packages(),
	include_package_data=True,
	install_requires=[
	'pandas',
	'networkx',
	'beautifulsoup4'
	],
)
