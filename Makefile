PYTHON ?= python3

.PHONY: validate test build check
validate:
	$(PYTHON) scripts/catalog.py validate
test:
	$(PYTHON) -m unittest discover -s tests -v
build:
	$(PYTHON) scripts/catalog.py build
check: validate test
