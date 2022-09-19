from setuptools import setup, find_namespace_packages

with open('README.md') as file:
    long_description = file.read()


setup(
    name='findcoord',
    version='0.2.0',
    description='Multi-plateform analysis tool',
    url='https://github.com/hameye/findcoord',
    author='Hadrien Meyer',
    author_email='jean.cauzid@univ-lorraine.fr',
    license='GPL v3',
    packages=find_namespace_packages(exclude=[
            'doc', 'doc.*']),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-image'
    ],
    zip_safe=False
)
