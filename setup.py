from distutils.command.install_data import install_data

from setuptools import setup, find_packages

VERSION = "0.1"
LICENSE = open("LICENSE").read()
README = open("README.md").read()

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
            'console_scripts': ['simplegeoip=simplegeoip:main'],
        },
        package_data={'': ['LICENSE', 'README.md']},
        # package_dir={'maxminddb': 'maxminddb'},
        include_package_data=True,
        zip_safe=False,
        # install_requires=requirements,
        license=LICENSE,
        cmdclass=cmdclass,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python',
            'Topic :: Internet :: Proxy Servers',
            'Topic :: Internet',
        ])