from pathlib import Path
from setuptools import setup, find_packages

with (Path(__file__).parent.resolve() / 'requirements.txt').open('r') as requirements:
    deps = [dep.strip('\n') for dep in requirements.readlines()]

setup(

    name='api-timeline',
    packages=find_packages(),
    include_package_data=True,
    install_requires=deps
)