# Advanced Usage

This page covers advanced usage of Charstyle for complex text styling.

## Creating Reusable Styles

```python
from charstyle import RED, GREEN, BLUE, BOLD, ITALIC, Style

# Create reusable styles
error_style = Style(color=RED, style=BOLD)
warning_style = Style(color=YELLOW, style=ITALIC)
success_style = Style(color=GREEN)

# Apply styles to text
print(error_style("Error: Operation failed"))
print(warning_style("Warning: This operation might take a while"))
print(success_style("Success: Operation completed"))
```

## Styling Parts of Text

### Using style_split

Split a string by a delimiter and apply different styles to each part:

```python
from charstyle import BOLD, GREEN, RED, style_split

# Style a key-value pair with different styles
print(style_split("Status: OK", ":", BOLD, GREEN))
print(style_split("Error: File not found", ":", (RED, BOLD), RED))
```

### Using style_complex

Style different parts of a string based on a regular expression pattern:

```python
from charstyle import BLUE, GREEN, YELLOW, style_complex

# Style with regular expression pattern
print(
    style_complex(
        "Status: OK (processed)",
        r"(: |\()",
        BLUE,   # "Status"
        GREEN,  # "OK "
        YELLOW, # "processed)"
    )
)
```

### Using style_pattern_match

Style different parts of a string based on named capture groups in a regular expression:

```python
from charstyle import RED, YELLOW, BOLD, style_pattern_match

pattern = r"(?P<code>\d{3}) (?P<status>\w+) - (?P<message>.*)"
style_map = {
    "code": (RED, BOLD),
    "status": RED,
    "message": YELLOW,
}
print(
    style_pattern_match(
        "404 NotFound - The requested resource does not exist", 
        pattern, 
        style_map
    )
)
```

### Using style_format

Style different parts of a string based on format placeholders:

```python
from charstyle import BLUE, GREEN, RED, BOLD, style_format

# Format with positional arguments
print(style_format("{} = {}", ("username", BLUE), ("admin", GREEN)))

# Format with keyword arguments
print(
    style_format(
        "HTTP/{version} {code} {status}",
        version=("1.1", BLUE),
        code=("200", GREEN),
        status=("OK", (GREEN, BOLD)),
    )
)
```

## Creating Custom Styling Functions

You can create your own styling functions for specific use cases:

```python
from charstyle import RED, GREEN, YELLOW, BOLD, colored

def status_message(status, message):
    """Format a status message with appropriate styling."""
    if status == "error":
        status_styled = colored("ERROR", color=RED, style=BOLD)
    elif status == "warning":
        status_styled = colored("WARNING", color=YELLOW, style=BOLD)
    elif status == "success":
        status_styled = colored("SUCCESS", color=GREEN, style=BOLD)
    else:
        status_styled = colored("INFO", color=BLUE, style=BOLD)
    
    return f"[{status_styled}] {message}"

# Use the custom function
print(status_message("error", "Failed to connect to the server"))
print(status_message("warning", "Connection timeout, retrying..."))
print(status_message("success", "Connected successfully"))
```

## Styling Tables

Create styled tables for terminal output:

```python
from charstyle import BLUE, GREEN, RED, YELLOW, BOLD, UNDERLINE, colored

def print_table_row(columns, widths, styles=None):
    """Print a styled table row."""
    if styles is None:
        styles = [None] * len(columns)
    
    row = []
    for col, width, style in zip(columns, widths, styles):
        text = str(col).ljust(width)
        if style:
            text = colored(text, **style)
        row.append(text)
    
    print(" | ".join(row))

def print_table_header(headers, widths):
    """Print a styled table header."""
    header_styles = [{"style": BOLD} for _ in headers]
    print_table_row(headers, widths, header_styles)
    
    # Print separator
    separator = []
    for width in widths:
        separator.append("-" * width)
    print_table_row(separator, widths)

# Example usage
headers = ["Name", "Status", "Memory", "CPU"]
widths = [20, 10, 10, 10]

print_table_header(headers, widths)

# Print rows with different styles
rows = [
    ["server1.example.com", "Running", "2.1 GB", "45%"],
    ["server2.example.com", "Stopped", "0.0 GB", "0%"],
    ["server3.example.com", "Warning", "7.8 GB", "92%"]
]

styles = [
    [None, {"color": GREEN}, None, None],
    [None, {"color": RED}, None, None],
    [None, {"color": YELLOW}, None, {"color": RED, "style": BOLD}]
]

for row, style in zip(rows, styles):
    print_table_row(row, widths, style)
```

## Next Steps

Now that you've learned about advanced styling techniques, you can explore:

- [Styling Options](styling-options.md) - Understand when to use Style objects vs. tuples
- [Complex Examples](../examples/complex.md) - See more complex styling examples
- [API Reference](../api/complex-styling.md) - Detailed API documentation for complex styling functions
