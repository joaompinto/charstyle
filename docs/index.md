# Charstyle Documentation

Welcome to the documentation for **Charstyle**, a Python library for styling terminal text output using ANSI escape sequences.

## Overview

Charstyle provides a simple and intuitive API for adding color, background color, and text styles (bold, italic, underline, etc.) to text output in terminal applications.

```python
from charstyle import RED, BOLD, colored

# Simple styling
print(colored("This is red and bold text", color=RED, style=BOLD))
```

## Features

- **Simple API**: Easy-to-use functions for styling text
- **Enum-based Constants**: Type-safe constants for colors and styles
- **Convenience Functions**: Shorthand functions for common styling operations
- **Complex Styling**: Advanced functions for styling parts of strings
- **Terminal Icons**: Built-in icons for terminal output

## Installation

```bash
pip install charstyle
```

## Quick Links

- [Getting Started](getting-started.md) - Learn the basics of Charstyle
- [Basic Usage](usage/basic.md) - Simple styling examples
- [Advanced Usage](usage/advanced.md) - Complex styling techniques
- [API Reference](api/core.md) - Detailed API documentation
