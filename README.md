# Charstyle

[![PyPI version](https://badge.fury.io/py/charstyle.svg)](https://badge.fury.io/py/charstyle)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/charstyle.svg)](https://pypi.org/project/charstyle/)

A simple Python library for styling terminal text output using ANSI escape sequences.

## Features

- Text colors (normal and bright variants)
- Background colors (normal and bright variants)
- Text styles (bold, italic, underline, etc.)
- Chainable style combinations
- Custom style definitions
- Complex string styling with multiple components
- Terminal icons/emojis that work in most modern terminals
- Windows 10+ compatibility

## Installation

**Requirements:** Python 3.11 or higher

```bash
pip install charstyle
```

For development and contributing to the project, see [README_DEVELOPERS.md](README_DEVELOPERS.md).

## Usage

### Basic Usage with Functions

```python
# Import the convenience functions and some constants
from charstyle import red, blue, green, yellow, bold, underline, italic
from charstyle import BLUE, UNDERLINE

# Apply basic styles
print(red("This is red text"))
print(blue("This is blue text"))
print(bold("This is bold text"))
print(underline("This is underlined text"))

# Combining with function parameters
print(red("Red text with underline", style=UNDERLINE))
print(bold("Bold blue text", color=BLUE))
```

### Using Style Constants

```python
# Import style constants and colored function
from charstyle import RED, BLUE, GREEN, YELLOW, BOLD, UNDERLINE, colored, BG_BLACK, BG_BLUE

# Apply styles with constants
print(colored("Red text", color=RED))
print(colored("Blue text", color=BLUE))
print(colored("Bold text", style=BOLD))
print(colored("Underlined text", style=UNDERLINE))

# Mix styles with colored function
print(colored("Bold yellow text", color=YELLOW, style=BOLD))
print(colored("Underlined red text", color=RED, style=UNDERLINE))

# Custom color and background
print(colored("Custom color and background", color=RED, bg_color=BLUE, style=BOLD))
```

### Advanced Usage

```python
from charstyle import YELLOW, BG_BLUE, BOLD, colored, Style, BRIGHT_RED, GREEN, ITALIC

# Combine foreground color, background color, and style
print(colored("Custom styling", 
              color=YELLOW, 
              bg_color=BG_BLUE, 
              style=BOLD))

# Create custom styles with Style class
error_style = Style(color=BRIGHT_RED, style=BOLD)
warning_style = Style(color=YELLOW, style=ITALIC)
success_style = Style(color=GREEN)

# Apply error style
error_message = "Error: Something went wrong!"
print(error_style(error_message))

# Apply warning style
print(warning_style("Warning: This is a warning message"))

# Apply success style
print(success_style("Success: Operation completed successfully"))
```

### Combining Multiple Styles

```python
from charstyle import (
    colored, bold, italic, RED, BOLD, ITALIC, UNDERLINE, 
    Style, BRIGHT_GREEN, BG_BLACK
)

# Method 1: Using the style parameter with a tuple of styles
print(colored("Bold and Italic", 
              style=(BOLD, ITALIC)))

# Method 2: Using the Style class
bold_italic = Style(style=(BOLD, ITALIC))
print(bold_italic("Bold and Italic (Style class)"))

# Method 3: Combining styles with colors
print(colored("Bold red italic", 
              color=RED, 
              style=(BOLD, ITALIC)))

# Fancy style with multiple attributes
fancy_style = Style(
    color=BRIGHT_GREEN,
    bg_color=BG_BLACK,
    style=(BOLD, UNDERLINE)
)
print(fancy_style("Bold underlined bright green text on black background"))
```

### Complex String Styling

```python
from charstyle import (
    style_split, style_complex, style_pattern_match, style_format,
    BOLD, GREEN, RED, BLUE, YELLOW, ITALIC, red, green, blue, yellow, bold, italic
)

# Split by delimiter and style each part differently
status = style_split("Status: Online", ":", BOLD, GREEN)
print(status)  # "Status" is bold, "Online" is green

# Style text using regex pattern
text = "The value is 42 and the status is OK"
styled = style_complex(text, r"(value is \d+)|(status is \w+)", 
                       RED, GREEN)
print(styled)  # "value is 42" is red, "status is OK" is green

# Style using pattern matching with named groups
log_line = "2023-02-27 15:30:45 [INFO] User authenticated"
styled_log = style_pattern_match(
    log_line,
    r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<message>.*)",
    {"date": BLUE, "time": GREEN, "level": YELLOW, "message": ITALIC}
)
print(styled_log)

# Style using format-style placeholders
from charstyle import style_format, BOLD, RED
template = "User {username} logged in from {ip}"
formatted = style_format(template, 
                         username=("admin", BOLD), 
                         ip=("192.168.1.100", RED))
print(formatted)  # "admin" is bold, "192.168.1.100" is red
```

### Terminal Icons

Charstyle includes a collection of widely supported terminal icons that display correctly in most modern terminals:

```python
from charstyle import Icon, colored, BOLD, RED, ITALIC

# Use individual icons
print(f"{Icon.CHECK} {colored('Task completed', style=BOLD)}")
print(f"{Icon.CROSS} {colored('Task failed', color=RED)}")
print(f"{Icon.WARNING} {colored('Warning message', style=ITALIC)}")

# Create a simple box
print(f"{Icon.TOP_LEFT}{Icon.H_LINE * 10}{Icon.TOP_RIGHT}")
print(f"{Icon.V_LINE}{' ' * 10}{Icon.V_LINE}")
print(f"{Icon.BOTTOM_LEFT}{Icon.H_LINE * 10}{Icon.BOTTOM_RIGHT}")
```

View all available icons:

```bash
python -m charstyle --icons
```

## Available Styles

### Text Colors
- BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
- BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE

### Background Colors
- BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN, BG_WHITE
- BG_BRIGHT_BLACK, BG_BRIGHT_RED, BG_BRIGHT_GREEN, BG_BRIGHT_YELLOW, BG_BRIGHT_BLUE, BG_BRIGHT_MAGENTA, BG_BRIGHT_CYAN, BG_BRIGHT_WHITE

### Text Styles
- BOLD
- DIM
- ITALIC
- UNDERLINE
- BLINK
- REVERSE
- HIDDEN
- STRIKETHROUGH

## Author

- **João Pinto** - [joaompinto](https://github.com/joaompinto)

## Development

For developers who want to contribute to this project, please see:

- [CONTRIBUTING.md](CONTRIBUTING.md) - Guidelines for contributing to the project
- [README_DEVELOPERS.md](README_DEVELOPERS.md) - Detailed guide for development workflows

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
