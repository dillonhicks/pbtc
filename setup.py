"""GRPC Tools Wrapper for building protobufs in setup.py"""
from setuptools import setup, find_packages


setup(
    name='pbtc',
    version='0.0.1',
    url='https://github.com/dillonhicks/pbtc',
    license='Apache License Version 2.0',
    author='Dillon Hicks',
    author_email='dillon@dillonhicks.io',
    description='grpc_tools wrapper building protobufs',
    long_description=__doc__,
    package_dir={'': '.'},
    namespace_packages=[],
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=['Cython', 'grpcio-tools'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
