# Core API

This page documents the core functions and constants in the Charstyle library.

## colored

The main function for applying styles to text.

```python
colored(text: str, color: ForegroundColor | None = None, bg_color: BackgroundColor | None = None, style: TextStyle | tuple[TextStyle, ...] | None = None) -> str
```

**Parameters:**
- `text` (str): The text to style
- `color` (ForegroundColor | None): The text color to apply
- `bg_color` (BackgroundColor | None): The background color to apply
- `style` (TextStyle | tuple[TextStyle, ...] | None): The text style(s) to apply

**Returns:**
- `str`: The styled text

**Example:**
```python
from charstyle import RED, BG_BLACK, BOLD, colored

# Basic usage
print(colored("Hello, World!", color=RED))

# With background color
print(colored("Warning", color=RED, bg_color=BG_BLACK))

# With text style
print(colored("Important", style=BOLD))

# Combining multiple styles
print(colored("Critical Error", color=RED, style=(BOLD, UNDERLINE)))
```

## supports_color

Check if the terminal supports color output.

```python
supports_color() -> bool
```

**Returns:**
- `bool`: True if the terminal supports color, False otherwise

**Example:**
```python
from charstyle import supports_color, RED, colored

if supports_color():
    print(colored("This text is red", color=RED))
else:
    print("This text is not colored because your terminal doesn't support colors")
```

## Style Enums

Charstyle provides various style constants through enums:

### TextStyle

Text style modifiers:

```python
from charstyle import NORMAL, BOLD, DIM, ITALIC, UNDERLINE, BLINK, REVERSE, HIDDEN, STRIKE

print(colored("Bold text", style=BOLD))
print(colored("Italic text", style=ITALIC))
print(colored("Underlined text", style=UNDERLINE))
```

### ForegroundColor

Text colors:

```python
from charstyle import BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from charstyle import BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE

print(colored("Red text", color=RED))
print(colored("Bright green text", color=BRIGHT_GREEN))
```

### BackgroundColor

Background colors:

```python
from charstyle import BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN, BG_WHITE
from charstyle import BG_BRIGHT_BLACK, BG_BRIGHT_RED, BG_BRIGHT_GREEN, BG_BRIGHT_YELLOW, BG_BRIGHT_BLUE, BG_BRIGHT_MAGENTA, BG_BRIGHT_CYAN, BG_BRIGHT_WHITE

print(colored("Text with red background", bg_color=BG_RED))
print(colored("Text with bright blue background", bg_color=BG_BRIGHT_BLUE))
```

## Convenience Functions

Charstyle provides convenience functions for common styling operations:

```python
from charstyle import red, green, blue, bold, italic, underline

print(red("This text is red"))
print(bold("This text is bold"))
print(green("This text is green", style=BOLD))  # Can combine with styles
```

For more advanced styling options, see the [Style Objects](style-objects.md) and [Complex Styling](complex-styling.md) pages.
