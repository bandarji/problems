.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build executable
	@go build -o ./problems main.go

clean: ## Remove unnecessary files
	@go clean
	@rm -f problems coverage.out coverage.html

run: build ## Play the game
	@./problems

test: ## Execute unit tests
	@go test -count=1 -coverprofile=coverage.out ./...
	@go tool cover -func=coverage.out

coverage: test ## Show code coverage in browser
	@go tool cover -html=coverage.out -o coverage.html
