#!/bin/bash
PACKAGE=pymathics-hello

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

python setup.py bdist_wheel --universal
mv -v dist/pymathics_hello-${__version__}-{py2.,}py3-none-any.whl
python ./setup.py sdist
finish
