from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='neonetic_io',
    version=version,
    description='Community portal for neonetic',
    author='neonetic® Pvt Ltd',
    author_email='connect@neonetic.co.za',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
