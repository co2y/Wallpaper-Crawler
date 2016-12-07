# coding=utf-8
import os
from setuptools import setup, find_packages
from dota2crawler import __version__, __author__, __email__

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()


ROOT = os.path.abspath(os.path.dirname(__file__))


setup(
    name='dota2crawler',
    version=__version__,
    author=__author__,
    author_email=__email__,
    keywords='dota2crawler',
    description='dota2 wallpaper crawler for wallpaperscraft.com',
    url='https://github.com/co2y/Wallpaper-Crawler',
    download_url='https://github.com/co2y/Wallpaper-Crawler/tarball/master',
    packages=find_packages(),
    package_data={'': ['LICENSES']},
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'dota2crawler = dota2crawler.__main__:run'
        ]
    },
    license='MIT License',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Other Audience',
        'Natural Language :: Chinese (Traditional)',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ),
)
