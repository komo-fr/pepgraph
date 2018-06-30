from setuptools import setup, find_packages

setup(
	name='pepgraph',
	version='0.0.1',
	package=find_packages(),
	include_package_data=True,
	install_requires=[
	'pandas',
	],
)
