# Damn 🥒able
A Web App that is Intentionally Vulnerable to Insecure Deserialization via Pickle attacks

## Vulnerabilities
The application contains the following vulnerabilities:
1. Vanilla Pickle RCE
2. Sour Pickles RCE (Custom Pickler only allows the following builtins to be imported `globals`, `getattr`, `dict`, `apply`)

## Installation
Installation is simple, clone the repo, create a virtual env, pip install
dependencies, and run the server.

```
# Clone the repo
git clone https://github.com/mynameiswillporter/DamnPickleable.git
cd DamnPickleable

# Create a virtualenv
python3 -m venv venv

# Activate the virtualenv
. venv/bin/activate        # Linux
venv\Scripts\activate      # Windows

# install dependencies
pip install -r requirements.txt

# run the server
python damn_pickleable.py
```

# Usage
After installation, run the server in the virtualenv using `python damn_pickleable.py`.
By default the server runs on port `8008`. Open your browswer and go to
`http://localhost:8008`. Upload some pickles and try to get RCE.
