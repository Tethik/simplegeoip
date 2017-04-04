from distutils.command.install_data import install_data

from setuptools import setup, find_packages

VERSION = "0.1.5"
with open("LICENSE") as f:
    LICENSE = f.read()
with open("README.rst") as f:
    README = f.read()

setup(
        name='simplegeoip',
        version=VERSION,
        author='Joakim Uddholm',
        author_email='tethik@gmail.com',
        description='Shell script and module for easy geoip lookups.',
        long_description=README,
        url='https://github.com/Tethik/simplegeoip',
        packages=['simplegeoip'],
        entry_points = {
            'console_scripts': ['simplegeoip=simplegeoip.main:script_entry'],
        },
        package_data={'': ['LICENSE', 'README.rst']},
        include_package_data=True,
        install_requires=[
            'maxminddb',
            'requests',
            'appdirs'
        ],
        tests_require=[
            'pytest',
            'pytest-cov',
        ],
        license=LICENSE,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python',
            'Topic :: Internet :: Proxy Servers',
            'Topic :: Internet',
        ])
