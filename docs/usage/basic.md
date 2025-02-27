# Basic Usage

This page covers the basic usage of Charstyle for styling terminal text.

## Importing Charstyle

```python
# Import the main colored function and style constants
from charstyle import colored, RED, GREEN, BLUE, BOLD, ITALIC

# Or import convenience functions
from charstyle import red, green, blue, bold, italic
```

## Basic Text Coloring

```python
from charstyle import RED, GREEN, BLUE, colored

# Color text
print(colored("This text is red", color=RED))
print(colored("This text is green", color=GREEN))
print(colored("This text is blue", color=BLUE))
```

## Text Styles

```python
from charstyle import BOLD, ITALIC, UNDERLINE, STRIKE, colored

# Apply text styles
print(colored("This text is bold", style=BOLD))
print(colored("This text is italic", style=ITALIC))
print(colored("This text is underlined", style=UNDERLINE))
print(colored("This text is strikethrough", style=STRIKE))
```

## Background Colors

```python
from charstyle import BG_RED, BG_GREEN, BG_BLUE, colored

# Apply background colors
print(colored("Text with red background", bg_color=BG_RED))
print(colored("Text with green background", bg_color=BG_GREEN))
print(colored("Text with blue background", bg_color=BG_BLUE))
```

## Combining Styles

```python
from charstyle import RED, BG_YELLOW, BOLD, UNDERLINE, colored

# Combine color, background, and style
print(colored("Important warning", color=RED, bg_color=BG_YELLOW, style=BOLD))

# Combine multiple text styles
print(colored("Critical error", color=RED, style=(BOLD, UNDERLINE)))
```

## Convenience Functions

```python
from charstyle import red, green, blue, bold, italic, underline

# Use convenience functions
print(red("This text is red"))
print(bold("This text is bold"))
print(green("This text is green"))

# Combine convenience functions
print(bold(red("This text is bold and red")))

# Add style parameter to convenience functions
print(blue("This text is blue and underlined", style=UNDERLINE))
```

## Checking Terminal Support

```python
from charstyle import supports_color, RED, colored

# Check if the terminal supports colors
if supports_color():
    print(colored("This text is red", color=RED))
else:
    print("This terminal doesn't support colors")
```

## Next Steps

Now that you've learned the basics of Charstyle, you can explore more advanced features:

- [Advanced Usage](advanced.md) - Learn about complex styling techniques
- [Styling Options](styling-options.md) - Understand when to use Style objects vs. tuples
- [API Reference](../api/core.md) - Detailed API documentation
