.PHONY: lint
lint:
	@pip install .[lint]
	@pycodestyle --verbose src/

.PHONY: test
test:
	@pip install .[test]
	@tox

.PHONY: clean
clean:
	@rm -rf dist
