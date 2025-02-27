# Complex Styling Examples

This page provides examples of complex styling techniques using Charstyle.

## Style Split Examples

Split a string by a delimiter and apply different styles to each part:

```python
from charstyle import BOLD, GREEN, RED, CYAN, ITALIC, style_split

# Style a key-value pair with different styles
print(style_split("Status: OK", ":", BOLD, GREEN))

# Style with multiple styles
print(
    style_split(
        "Error: File not found",
        ":",
        (RED, BOLD),  # Using a tuple of styles
        ITALIC,
    )
)

# Multiple delimiters with different styles
print(style_split("Name: John Doe (Developer)", ":", CYAN, BOLD))
```

Output:
```
Status: OK
Error: File not found
Name: John Doe (Developer)
```

## Complex Pattern Styling

Style different parts of a string based on a regular expression pattern:

```python
from charstyle import BLUE, GREEN, YELLOW, CYAN, MAGENTA, RED, BOLD, style_complex

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

# Log entry styling
print(
    style_complex(
        "[INFO] User login: admin",
        r"(\[|\] |\: )",
        CYAN,    # "INFO"
        MAGENTA, # "User login"
        GREEN,   # "admin"
    )
)

# Server configuration
print(
    style_complex(
        "Server=production; Port=8080; Active=true",
        r"(=|; )",
        (BLUE, BOLD), # "Server"
        GREEN,        # "production"
        (BLUE, BOLD), # "Port"
        YELLOW,       # "8080"
        (BLUE, BOLD), # "Active"
        RED,          # "true"
    )
)
```

Output:
```
Status: OK (processed)
[INFO] User login: admin
Server=production; Port=8080; Active=true
```

## Pattern Matching with Named Groups

Style different parts of a string based on named capture groups in a regular expression:

```python
from charstyle import RED, YELLOW, BRIGHT_RED, BOLD, WHITE, GREEN, BRIGHT_BLACK, style_pattern_match

# HTTP status code styling
pattern = r"(?P<code>\d{3}) (?P<status>\w+) - (?P<message>.*)"
style_map = {
    "code": (BRIGHT_RED, BOLD),
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

# Log entry styling
pattern = r"(?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+): (?P<message>.*)"
style_map = {
    "time": BRIGHT_BLACK,
    "level": (GREEN, BOLD),
    "message": WHITE,
}
print(
    style_pattern_match(
        "14:25:36 INFO: User authentication successful", 
        pattern, 
        style_map
    )
)
```

Output:
```
404 NotFound - The requested resource does not exist
14:25:36 INFO: User authentication successful
```

## Format-based Styling

Style different parts of a string based on format placeholders:

```python
from charstyle import BLUE, GREEN, RED, BOLD, YELLOW, BRIGHT_BLACK, style_format

# Format with positional arguments
print(style_format("{} = {}", ("username", BLUE), ("admin", GREEN)))

# Format with keyword arguments
print(
    style_format(
        "HTTP/{version} {code} {status}",
        version=("1.1", BRIGHT_BLACK),
        code=("200", GREEN),
        status=("OK", (GREEN, BOLD)),
    )
)

# Command line example
print(
    style_format(
        "{command} {arg1} {arg2}",
        command=("git", (RED, BOLD)),
        arg1=("commit", YELLOW),
        arg2=("-m", BLUE),
    )
)
```

Output:
```
username = admin
HTTP/1.1 200 OK
git commit -m
```

## Combining Different Techniques

You can combine different styling techniques for more complex output:

```python
from charstyle import RED, GREEN, BLUE, YELLOW, BOLD, ITALIC, style_split, style_format

# Combine style_split with style_format
header = style_format("{} {}", ("System", (BLUE, BOLD)), ("Status", BLUE))
value = style_split("State: Running", ":", (YELLOW, ITALIC), GREEN)
print(f"{header}: {value}")

# Create a styled table row
def styled_row(key, value, status):
    key_styled = style_format("{}", (key, (BLUE, BOLD)))
    value_styled = style_format("{}", (value, YELLOW))
    if status == "ok":
        status_styled = style_format("[{}]", ("OK", GREEN))
    else:
        status_styled = style_format("[{}]", ("FAIL", RED))
    return f"{key_styled}: {value_styled} {status_styled}"

print(styled_row("CPU", "2.4 GHz", "ok"))
print(styled_row("Memory", "16 GB", "ok"))
print(styled_row("Disk", "95% full", "fail"))
```

Output:
```
System Status: State: Running
CPU: 2.4 GHz [OK]
Memory: 16 GB [OK]
Disk: 95% full [FAIL]
```
