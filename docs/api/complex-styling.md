# Complex Styling API

This page documents the complex styling functions available in Charstyle.

## style_split

Split a string by a delimiter and apply different styles to each part.

```python
style_split(text: str, delimiter: str, *styles: StyleType) -> str
```

**Parameters:**
- `text` (str): The text to style
- `delimiter` (str): The delimiter to split the text by
- `*styles` (StyleType): The styles to apply to each part

**Returns:**
- `str`: The styled text

**Example:**
```python
from charstyle import BOLD, GREEN, RED, style_split

# Style a key-value pair with different styles
print(style_split("Status: Success", ":", BOLD, GREEN))
print(style_split("Error: File not found", ":", (RED, BOLD), RED))
```

## style_complex

Style different parts of a string based on a regular expression pattern.

```python
style_complex(text: str, pattern: str, *styles: StyleType) -> str
```

**Parameters:**
- `text` (str): The text to style
- `pattern` (str): The regular expression pattern to split the text by
- `*styles` (StyleType): The styles to apply to each part

**Returns:**
- `str`: The styled text

**Example:**
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

## style_pattern_match

Style different parts of a string based on named capture groups in a regular expression.

```python
style_pattern_match(text: str, pattern: str, style_map: Dict[str, StyleType]) -> str
```

**Parameters:**
- `text` (str): The text to style
- `pattern` (str): The regular expression pattern with named capture groups
- `style_map` (Dict[str, StyleType]): A mapping from group names to styles

**Returns:**
- `str`: The styled text

**Example:**
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

## style_format

Style different parts of a string based on format placeholders.

```python
style_format(format_str: str, *args, **kwargs) -> str
```

**Parameters:**
- `format_str` (str): The format string with placeholders
- `*args`: Positional arguments as tuples of (value, style)
- `**kwargs`: Keyword arguments as tuples of (value, style)

**Returns:**
- `str`: The styled text

**Example:**
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
