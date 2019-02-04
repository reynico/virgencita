.PHONY: lint
lint:
	@pip install .[lint]
	@pycodestyle --verbose src/

.PHONY: test
test:
	@pip install .[test]
	@tox

.PHONY: install
install:
	@python3 setup.py install

.PHONY: clean
clean:
	@rm -rf dist

.PHONY: container
container:
	@docker build -t virgencita .
