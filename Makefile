install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

#install-azure:
#	pip install --upgrade pip &&\
#		pip install -r requirements-azure.txt

format:
	black *.py

lint:
	pylint --disable=R,C code.py
	pylint --disable=R,C test_code.py

test:
	python -m pytest -vv --cov=code test_code.py

all: install lint test
