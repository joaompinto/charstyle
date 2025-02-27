# Styling Options

Charstyle provides multiple ways to apply styles to your text. This guide explains when to use each approach.

## Style Constants

The most basic way to style text is using the built-in style constants:

```python
from charstyle import RED, BOLD, colored

# Using a color constant
print(colored("This is red text", color=RED))

# Using a text style constant
print(colored("This is bold text", style=BOLD))
```

## Combining Styles

When you need to apply multiple styles to the same text, you have two options: using `Style` objects or using tuples of style constants.

### Style Objects vs. Tuples

Both approaches allow you to combine styles, but they have different use cases and advantages.

## When to Use Style Objects

The `Style` class provides a way to create reusable style combinations with explicit control over all aspects of styling.

### 1. When you need to combine color, background color, and text style separately

```python
from charstyle import RED, BG_BLACK, BOLD, Style

# Style object allows explicit specification of each component
error_style = Style(color=RED, bg_color=BG_BLACK, style=BOLD)
print(error_style("Error: Operation failed"))
```

### 2. When you need to reuse the same style combination multiple times

```python
from charstyle import YELLOW, BOLD, ITALIC, Style

# Define once, use many times
warning_style = Style(color=YELLOW, style=(BOLD, ITALIC))
print(warning_style("Warning: This operation might take a while"))
print(warning_style("Warning: Insufficient disk space"))
```

### 3. When you need to specify background colors

```python
from charstyle import BLACK, BG_YELLOW, Style

# Style objects make it clearer when specifying background colors
highlight_style = Style(color=BLACK, bg_color=BG_YELLOW)
print(highlight_style("IMPORTANT NOTICE"))
```

### 4. When you need more complex style combinations

```python
from charstyle import BRIGHT_GREEN, BG_BLUE, BOLD, UNDERLINE, Style

# Multiple text styles with both foreground and background colors
complex_style = Style(color=BRIGHT_GREEN, bg_color=BG_BLUE, style=(BOLD, UNDERLINE))
print(complex_style("SUCCESS: All tests passed"))
```

## When to Use Tuples

Tuples provide a more concise way to combine styles for one-off usage.

### 1. When you only need to combine text styles (no colors)

```python
from charstyle import BOLD, ITALIC, colored

# Simple combination of text styles
print(colored("Important note", style=(BOLD, ITALIC)))
```

### 2. When you need a simple combination of a color and a text style

```python
from charstyle import RED, BOLD, colored

# Concise way to specify color + style
print(colored("Error", style=(RED, BOLD)))
```

### 3. When you want more concise, inline styling

```python
from charstyle import BLUE, BOLD, GREEN, style_format

# More compact for one-off usage
print(style_format("{header} {value}", 
                  header=("Title:", (BLUE, BOLD)), 
                  value=("Content", GREEN)))
```

### 4. When you're using style_complex, style_split, or other functions that accept multiple styles

```python
from charstyle import BLUE, BOLD, GREEN, style_complex

# Cleaner when passing multiple styles to functions
print(style_complex("Key=Value", r"=", (BLUE, BOLD), GREEN))
```

## General Rule of Thumb

- **Use Style objects** when you need explicit control over all aspects of styling (foreground color, background color, and text style) or when you need to reuse the style.
- **Use tuples** for simpler, one-off style combinations, especially when you're just combining a color with a text style.

The tuple approach is generally more concise and readable for simple cases, while the Style object provides more flexibility and clarity for complex styling needs.

## Examples

### Style Object Example

```python
from charstyle import RED, BG_BLACK, BOLD, Style

# Create a reusable error style
error_style = Style(color=RED, bg_color=BG_BLACK, style=BOLD)

# Apply the style to different messages
print(error_style("ERROR: File not found"))
print(error_style("ERROR: Permission denied"))
```

### Tuple Example

```python
from charstyle import RED, BOLD, colored, style_split

# One-off styling with a tuple
print(colored("Error message", style=(RED, BOLD)))

# Using tuples with style_split
print(style_split("Status: Success", ":", (BOLD, RED), (GREEN, BOLD)))
```
