# A GNU Makefile to run various tasks - compatibility for us old-timers.

# Note: This makefile include remake-style target comments.
# These comments before the targets start with #:
# remake --tasks to shows the targets and the comments

GIT2CL ?= admin-tools/git2cl
PYTHON ?= python3
PIP ?= pip3
RM  ?= rm
LANG = en

.PHONY: all build \
   check clean \
   develop dist doc doc-data \
   pypi-setup \
   pytest \
   rmChangeLog \
   test

#: Default target - same as "develop"
all: develop

#: build everything needed to install
build:
	$(PYTHON) ./setup.py build

#: Check Python version, and install PyPI dependencies
pypi-setup:
	$(PIP) install -e .

#: Set up to run from the source tree
develop: pypi-setup
	$(PIP) install -e .

#: Install mathics
install:
	$(PYTHON) setup.py install

# Run tests
check: pytest

#: Remove derived files
clean: clean-pyc

#: Remove old PYC files
clean-pyc:
	@find . -name "*.pyc" -type f -delete

#: Run py.test tests. Use environment variable "o" for pytest options
pytest:
	py.test test $o


# #: Make Mathics PDF manual
# doc mathics.pdf: mathics/doc/tex/data
# 	(cd mathics/doc/tex && $(MAKE) mathics.pdf)

#: Remove ChangeLog
rmChangeLog:
	$(RM) ChangeLog || true

#: Create a ChangeLog from git via git log and git2cl
ChangeLog: rmChangeLog
	git log --pretty --numstat --summary | $(GIT2CL) >$@
