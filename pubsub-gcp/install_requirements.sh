#!/bin/bash

pip3 install virtualenv
virtualenv env
source env/bin/activate
env/bin/pip3 install -r requirements.txt