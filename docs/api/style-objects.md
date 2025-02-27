# Style Objects API

This page documents the `Style` class and related functionality in the Charstyle library.

## Style Class

The `Style` class allows you to create reusable style combinations with explicit control over colors and text styles.

### Constructor

```python
Style(color=None, bg_color=None, style=None)
```

**Parameters:**

- `color` (ForegroundColor | None): The text color to apply
- `bg_color` (BackgroundColor | None): The background color to apply
- `style` (TextStyle | tuple[TextStyle, ...] | str | None): The text style(s) to apply

### Usage

```python
from charstyle import RED, BG_BLACK, BOLD, Style

# Create a style
error_style = Style(color=RED, bg_color=BG_BLACK, style=BOLD)

# Apply the style to text
styled_text = error_style("Error message")
print(styled_text)
```

### Methods

#### `__call__(text: str) -> str`

Applies the style to the given text.

**Parameters:**
- `text` (str): The text to style

**Returns:**
- `str`: The styled text

## Style Constants

Charstyle provides various style constants through enums:

### TextStyle

Text style modifiers available as constants:

- `NORMAL` - Normal text (reset)
- `BOLD` - Bold text
- `DIM` - Dimmed text
- `ITALIC` - Italic text
- `UNDERLINE` - Underlined text
- `BLINK` - Blinking text
- `REVERSE` - Reversed colors
- `HIDDEN` - Hidden text
- `STRIKE` - Strikethrough text

### ForegroundColor

Text colors available as constants:

- `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`
- Bright variants: `BRIGHT_BLACK`, `BRIGHT_RED`, `BRIGHT_GREEN`, etc.

### BackgroundColor

Background colors available as constants:

- `BG_BLACK`, `BG_RED`, `BG_GREEN`, `BG_YELLOW`, `BG_BLUE`, `BG_MAGENTA`, `BG_CYAN`, `BG_WHITE`
- Bright variants: `BG_BRIGHT_BLACK`, `BG_BRIGHT_RED`, `BG_BRIGHT_GREEN`, etc.

## Combining Styles

You can combine styles in two ways:

### Using Style Objects

```python
from charstyle import RED, BG_BLACK, BOLD, UNDERLINE, Style

# Combining color, background, and multiple text styles
style = Style(color=RED, bg_color=BG_BLACK, style=(BOLD, UNDERLINE))
print(style("Important error message"))
```

### Using Tuples

```python
from charstyle import RED, BOLD, UNDERLINE, colored

# Combining styles with a tuple
print(colored("Important error message", color=RED, style=(BOLD, UNDERLINE)))
```

For more information on when to use each approach, see the [Styling Options](../usage/styling-options.md) guide.
