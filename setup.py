from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in property_customizations/__init__.py
from property_customizations import __version__ as version

setup(
	name="property_customizations",
	version=version,
	description="Property",
	author="Property",
	author_email="prop@mail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
