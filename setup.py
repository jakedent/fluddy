#!/usr/bin/python3
# noreorder
from fluddy.bud import initialize_flask_buddy
from setuptools import find_packages
import setuptools


initialize_flask_buddy()


setuptools.setup(
    name='fluddy',
    version='0.0.3',
    author='Jacob Dent',
    author_email='info@jacobdent.com',
    packages=find_packages(),
    package_data={
        '': ['LICENSE'],
    },
    url='https://github.com/jakedent/fluddy',
    license='MIT',
    entry_points={
        'console_scripts': [
            'fluddy = fluddy.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    description='Flask Buddy - CLI for managing Flask Apps.',
    include_package_data=True,
    zip_safe=True,
    long_description='''
    Flask is fast becoming the most popular web development framework for Python. Developers will typically manage multiple Flask apps individually where each app will rely on its own virtual environment - this can become tedius when launching and updating multiple Flask Apps in development. 
    \n
    Flask Buddy (fluddy) allows developers to launch and update their individual Flask Apps through a simple Command-Line Interface. CLI functionality also allows developers to create a launchable 'Hello from Fluddy' Flask App and to add previously created Flask Apps to fluddy for painless launches and updates.
    \n
    Full README and usage details: https://github.com/jakedent/fluddy
    ''',
    python_requires='>=3.5',

)
