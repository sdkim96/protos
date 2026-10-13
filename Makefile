.PHONY: lint format breaking generate check

lint:
	buf lint

format:
	buf format -w .

breaking:
	buf breaking --against '.git#branch=main'

generate:
	buf generate

check: generate
	buf build
	buf format -d --exit-code
	buf lint
	buf breaking --against '.git#branch=main'
	git diff --exit-code -- gen/
