.PHONY: build py-check py-push py-push-v

build:
	python3 -m build

py-check:
	python -m twine check dist/* 

py-push:
	python -m twine upload dist/*

py-push-v:
	python -m twine upload dist/* --verbose