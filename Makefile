build:
	@python translate.py --batch --output=aquesta ./src/aquesta.py
	@mv ./aquesta ./bin

test: build retest

retest:
	@./bin/aquesta tests/add.aq
