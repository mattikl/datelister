# datelister

Simple script to print a range of dates

Currently just passes the values to [Arrow](http://crsmithdev.com/arrow):

* `--format` is a format string of [Arrow tokens](http://crsmithdev.com/arrow/#tokens) 
* `--frame` (timeframe) can be any `datetime` (Python STD) property

## Usage

    $ datelister --help

Prints the following seven days if called without arguments:

    $ datelister

    $ datelister -s 2015-10-01 -e 2015-10-31

## Install

    $ python setup.py install

## Developing

Set up virtualenv in the `datelister` directory:

    $ virtualenv env
    $ . env/bin/activate
    $ pip install --editable .
