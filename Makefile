.PHONY: help lint


help:
	@echo "Available make targets:"
	@echo "  lint                  Perform static code analysis."
	@echo "Use 'make <target>' to run a specific command."

lint:
	python -m pip install pre-commit && \
	pre-commit run --all-files --verbose --show-diff-on-failure
