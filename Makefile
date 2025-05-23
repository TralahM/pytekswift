build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf build dist

deploy: clean build
	twine upload dist/*
