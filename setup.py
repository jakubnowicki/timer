from setuptools import setup

setup(
    name = 'timer',
    version = '0.1.0',
    packages = ['timer'],
    install_requires=[
        'Click',
        'tqdm'
    ],
    entry_points = {
        'console_scripts': [
            'timer = timer.timer:main'
        ]
    })
