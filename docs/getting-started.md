# Getting Started with Charstyle

This guide will help you get started with Charstyle, a Python library for styling terminal text.

## Installation

Install Charstyle using pip:

```bash
pip install charstyle
```

## Basic Usage

Here's a simple example to get you started:

```python
from charstyle import RED, GREEN, BLUE, BOLD, colored

# Basic color
print(colored("This is red text", color=RED))

# Color with style
print(colored("This is bold blue text", color=BLUE, style=BOLD))

# Using convenience functions
from charstyle import red, blue, bold

print(red("This is red text"))
print(bold("This is bold text"))
print(blue("This is blue text", style=BOLD))  # Can combine functions with styles
```

## Next Steps

Now that you've seen the basics, you can explore more advanced features:

- [Basic Usage Guide](usage/basic.md) - Learn about all the basic styling options
- [Advanced Usage](usage/advanced.md) - Discover complex styling techniques
- [Styling Options](usage/styling-options.md) - Understand when to use Style objects vs. tuples

## Requirements

- Python 3.11 or higher (required for StrEnum support)
- A terminal that supports ANSI color codes
