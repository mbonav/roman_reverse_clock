install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format: 
	black *.py

test:
	python -m pytest -vv --cov=hello hello.py
	#python -m pytest --nbval notebook.ipynb

lint:
	pylint --disable=R,C hello.py

all: install lint format test
