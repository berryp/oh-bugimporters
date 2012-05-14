#!/bin/sh

virtualenv env
env/bin/python setup.py develop
env/bin/python setup.py test
