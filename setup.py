from setuptools import setup, find_packages

setup(
    name='datelister',
    version='0.0.1',
    author='Matti Korttila',
    author_email='matti.korttila@gmail.com',
    url='https://github.com/mattikl/datelister',
    license='MIT License',
    py_modules=['datelister'],
    include_package_data=True,
    install_requires=[
        'click',
        'arrow',
    ],
    entry_points='''
        [console_scripts]
        datelister=datelister:cli
    ''',
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Natural Language :: English',
        'Topic :: Utilities',
    ),
)
