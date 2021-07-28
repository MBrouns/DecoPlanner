import os

from setuptools import setup, find_packages

base_packages = []
dev_packages = [
    'pytest',
    'flake8',
    'mypy'
]
base_packages.append("click")


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='decoPlanner',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=base_packages,
    extras_require={
      'dev': dev_packages
    },
    entry_points={
        'console_scripts': [
            'deco = decoPlanner.command:main',
        ]
    },
    description='',
    author='Matthijs Brouns',
    long_description=read('readme.md'),
    long_description_content_type='text/markdown',
)
