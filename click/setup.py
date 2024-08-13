from setuptools import setup

setup(
    name='userconnect', # app/script name
    version='0.1.0', # version
    py_modules=['set_conn'], # python modules, which must be executed
    install_requires=[ # script requirements
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'userconnect = set_conn:cli', # command1 = module1:cli
        ],
    },
)

# python3 -m venv .venv
# . .venv/bin/activate
# pip install --editable .