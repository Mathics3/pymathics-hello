#!/bin/bash
PACKAGE=Mathics3-Module-hello

# FIXME put some of the below in a common routine
function finish {
  cd $mathics_hello_owd
}

cd $(dirname ${BASH_SOURCE[0]})
mathics_hello_owd=$(pwd)
trap finish EXIT

if ! source ./pyenv-versions ; then
    exit $?
fi


cd ..
source pymathics/hello/version.py
echo $__version__

if ! pyenv local $pyversion ; then
    exit $?
fi

pyenv local 3.13
pip wheel --wheel-dir=dist .
python -m build --sdist
finish
