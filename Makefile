.PHONY: lint
lint:
	@pip install -q .[lint]
	@pycodestyle --verbose src/

.PHONY: test
test:
	@pip install -q .[test]
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
