"""Shared pytest fixtures and configuration for x64dbg-docs tests."""

import os
import tempfile
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files.
    
    Yields:
        Path: Path to the temporary directory.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def mock_sphinx_config(tmp_path: Path) -> dict:
    """Create a mock Sphinx configuration dictionary.
    
    Args:
        tmp_path: Pytest's tmp_path fixture.
        
    Returns:
        dict: Mock Sphinx configuration.
    """
    return {
        'project': 'Test Project',
        'copyright': '2024, Test Author',
        'author': 'Test Author',
        'version': '1.0',
        'release': '1.0.0',
        'extensions': ['recommonmark'],
        'source_suffix': ['.rst', '.md'],
        'master_doc': 'index',
        'html_theme': 'sphinx_rtd_theme',
        'html_static_path': ['_static'],
        'exclude_patterns': ['_build', 'Thumbs.db', '.DS_Store'],
    }


@pytest.fixture
def sample_markdown_content() -> str:
    """Provide sample markdown content for testing.
    
    Returns:
        str: Sample markdown content.
    """
    return """# Sample Documentation

## Introduction
This is a sample markdown file for testing purposes.

### Features
- Feature 1
- Feature 2
- Feature 3

## Code Example
```python
def hello_world():
    print("Hello, World!")
```

## Links
[Example Link](https://example.com)
"""


@pytest.fixture
def sample_rst_content() -> str:
    """Provide sample reStructuredText content for testing.
    
    Returns:
        str: Sample RST content.
    """
    return """Sample Documentation
===================

Introduction
------------
This is a sample RST file for testing purposes.

Features
--------
* Feature 1
* Feature 2
* Feature 3

Code Example
------------
.. code-block:: python

   def hello_world():
       print("Hello, World!")

Links
-----
`Example Link <https://example.com>`_
"""


@pytest.fixture
def project_root() -> Path:
    """Get the project root directory.
    
    Returns:
        Path: Path to the project root.
    """
    return Path(__file__).parent.parent


@pytest.fixture
def mock_command_docs() -> dict:
    """Provide mock command documentation data.
    
    Returns:
        dict: Mock command documentation.
    """
    return {
        'name': 'test_command',
        'description': 'A test command for documentation',
        'syntax': 'test_command [options] <args>',
        'options': {
            '-h, --help': 'Show help message',
            '-v, --verbose': 'Enable verbose output',
        },
        'examples': [
            'test_command -h',
            'test_command -v file.txt',
        ],
    }


@pytest.fixture(autouse=True)
def clean_environment(monkeypatch):
    """Clean environment variables that might affect tests.
    
    Args:
        monkeypatch: Pytest monkeypatch fixture.
    """
    env_vars_to_remove = [
        'SPHINX_BUILD',
        'READTHEDOCS',
        'SPHINXOPTS',
    ]
    for var in env_vars_to_remove:
        monkeypatch.delenv(var, raising=False)


@pytest.fixture
def sphinx_build_dir(temp_dir: Path) -> Path:
    """Create a Sphinx build directory structure.
    
    Args:
        temp_dir: Temporary directory fixture.
        
    Returns:
        Path: Path to the Sphinx build directory.
    """
    build_dir = temp_dir / '_build'
    build_dir.mkdir()
    (build_dir / 'html').mkdir()
    (build_dir / 'doctrees').mkdir()
    return build_dir