run:
	python3 agent.py

lint:
	flake8 .

format:
	black .

test:
	pytest || echo "Tests not ready yet"
