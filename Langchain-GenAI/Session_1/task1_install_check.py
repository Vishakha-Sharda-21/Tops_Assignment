"""
Session 1 - Task 1
Install LangChain in a new virtual environment and print its version.

Setup (run once, in a fresh venv):
    python -m venv venv
    source venv/bin/activate        # on Windows: venv/Scripts/activate
    pip install langchain
"""

import langchain

print(f"LangChain version installed: {langchain.__version__}")
