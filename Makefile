.PHONY: lint
lint:
	@pip install .[lint]
	@pycodestyle --verbose virgencita/

.PHONY: test
test:
	@pip install .[test]
	@tox

.PHONY: clean
clean:
	@rm -rf dist
