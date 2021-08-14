from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in qrcode_gen/__init__.py
from qrcode_gen import __version__ as version

setup(
	name="qrcode_gen",
	version=version,
	description="generate QR Code through api request",
	author="Ebkar Technologies",
	author_email="admin@ebkar.ly",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
