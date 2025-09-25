# Project 1 – Student Agent

This repo contains my Project 1 submission.

## Commands
- `agent.py accept request.json` → Accept and verify signed request  
- `agent.py scaffold` → Scaffold repo structure  
- `agent.py push` → Push repo to GitHub  
- `agent.py pages` → Enable GitHub Pages  
- `agent.py notify` → Notify evaluator  

## Setup
```bash
pip install -r requirements.txt


cat > requirements.txt << 'EOF'
click
cryptography
requests
flake8
black
pytest
