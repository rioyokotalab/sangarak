from setuptools import setup

setup(
    name='sangarak',
    version='0.1',
    description='Python library for reading matrices from many files and generating a single numpy matrix',
    license='BSD 3-clause',
    packages=['sangarak'],
    author='Sameer Deshmukh',
    author_email='sameer.desmukh93@gmail.com',
    keywords=['numpy', 'mpi', 'matrix'],
    install_requires=[
        'numpy',
    ],
    url='https://github.com/rioyokotalab/sangarak',
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)
