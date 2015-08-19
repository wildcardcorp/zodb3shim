from setuptools import setup, find_packages

version = '3.99.9'

install_requires = [
    "ZODB"
]

setup(
    version=version,
    name='ZODB3',
    long_description='',
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=False,
    zip_safe=True
)
