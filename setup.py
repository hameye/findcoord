from setuptools import setup, find_namespace_packages

setup(
    name='findcoord',
    version='0.0.1',
    description='FindCoord',
    url='git@github.com:hameye/findcoord.git',
    author='Deeplimers',
    author_email='meyerhadrien96@gmail.com',
    license='unlicense',
    packages=find_namespace_packages(exclude=[
            'doc', 'doc.*']),
    zip_safe=False
)
